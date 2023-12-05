import sys
import os

current_dir = os.path.dirname(os.path.abspath(_file_))
parent_dir = os.path.dirname(current_dir)
vm_dir = os.path.join(parent_dir, 'vm')
sys.path.append(vm_dir)

from vm import VirtualMachine
from assembler import Assembler
from architecture import NUM_REG, OPS, OP_MASK, OP_SHIFT, RAM_LEN

# converts the VM instructions to assembly code 
class Dissassembler:
    def dissassembler(self, lines):
        lines = self._get_lines(lines)
        labels = self._find_labels(lines)
        disassembled_code = self._disassemble_instruction(lines, labels) 
        return disassembled_code
# [/class]

    # [labels]
    # sample return 12: '@L001', 14: '@L002'
    def _find_labels(self, lines):
        label_nr = 0
        synthetic_labels = {}
        for n, ln in enumerate(lines):
            label, start_pos, end_pos = self._is_label(ln, n)
            if label:
                label_nr += 1
                start_pos_list = [value[0] for value in synthetic_labels.values()]
                assert start_pos not in start_pos_list, f'Duplicated label at the same position'
                synthetic_labels[f"@L{label_nr:03}"] = [start_pos, end_pos]
        for i in synthetic_labels:
            synthetic_labels[i] = [synthetic_labels[i][0], synthetic_labels[i][1] + label_nr]
        return synthetic_labels
        
    # sample return 0x9, 12
    def _is_label(self, ln, end_pos):
        # 0x8 = beq, 0x9 = bne
        control_flow_instructions = [0x8,0x9]
        for i in control_flow_instructions:
            if ln[-1] == i:
            # if instruction is 0,2,0,2,0,9, the first two digits represent lable in the third line 
                start_pos = ln[0]
                return True, start_pos, end_pos
        return False, None, None

    # [/labels]
    # Convert a single machine code instruction back into an assembly instruction
    def _disassemble_instruction(self, lines, labels=None):
        out = [[] for _ in range((len(lines)+len(labels)))]
        for label in labels:
            out[labels[label][0]] = label[1:] + ':'
            out[labels[label][1]].append(label)

        n = 0
        for ln in lines:
            if len(out[n]) > 0:
                if out[n][0][0] == 'L':
                    n += 1
            
            op, args = ln[-1], ln[:-1]
            args.reverse()
            code = ln[-1]

            instruction = next(key for key, value in OPS.items() if isinstance(value, dict) and op in value.values())
            fmt = next(value['fmt'] for key, value in OPS.items() if isinstance(value, dict) and op in value.values())

            if fmt == "--":
                for arg in args:
                    assert arg == 0, "Argument should be zero"
                out[n] = self._combine(instruction)


            elif fmt == "r-":
                assert args[-1] == 0, "Argument should be zero"
                assert 0 <= args[0] <= NUM_REG, f"Illegal register"
                out[n] = self._combine(instruction, 'R'+str(args[0]))

            elif fmt == "rr":
                assert 0 <= args[0] <= NUM_REG, f"Illegal register"
                assert 0 <= args[1] <= NUM_REG, f"Illegal register"
                out[n] = self._combine(instruction, 'R'+str(args[0]), 'R'+str(args[1]))
            
            elif fmt == "rv":
                assert 0 <= args[0] <= NUM_REG, f"Illegal register"
                if len(out[n]) == 0:
                    out[n] = self._combine(instruction, 'R'+str(args[0]), str(args[1]))
                else:
                    out[n] = self._combine(instruction, 'R'+str(args[0]), out[n][0])
            n += 1
        return out

    def label_location(self,lines):
        synthetic_labels = self._find_labels(self, lines)
        if ln in synthetic_labels.values():
            key = list(synthetic_labels.keys()) [list(synthetic_labels.values()).index(ln)]
            return True, key 

    # [combine]
    def _combine(self, *args):
        assert len(args) > 0, "Cannot combine no arguments"
        result = ''
        for i, a in enumerate(args):
            if i > 0:
                result += ' '
            result += a
        return result
    # [/combine]

    def _get_lines(self, lines):
        lines = [ln.strip() for ln in lines]
        lines = [ln for ln in lines if len(ln) > 0]
        lines = [ln for ln in lines if not self._is_comment(ln)]
        for ln in lines:
            assert not len(ln) > 6, 'Arguments too long'
        lines = [[int(ln[:2]), int(ln[2:4]), int(ln[-2]+'x'+ln[-1], 16)] for ln in lines]
        return lines


    def _is_comment(self, line):
        return line.startswith("#")
    


def main(dissassembler_cls):
    assert len(sys.argv) == 3, f"Usage: {sys.argv[0]} input|- output|-"
    reader = open(sys.argv[1], "r") if (sys.argv[1] != "-") else sys.stdin
    writer = open(sys.argv[2], "w") if (sys.argv[2] != "-") else sys.stdout
    lines = reader.readlines()
    dissassembler = dissassembler_cls()
    program = dissassembler.dissassembler(lines)
    for instruction in program:
        print(instruction, file=writer)


if __name__ == "__main__":    
    main(Dissassembler)
