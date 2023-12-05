import sys
import os
import pytest

current_dir = os.path.dirname(os.path.abspath(_file_))
print(current_dir)
parent_dir = os.path.dirname(current_dir)
print(parent_dir)
vm_dir = os.path.join(parent_dir, 'vm')
sys.path.append(vm_dir)
print(vm_dir)
print(sys.path)

from vm import VirtualMachine
from assembler import Assembler
from architecture import NUM_REG, OPS, OP_MASK, OP_SHIFT, RAM_LEN


def test_out_of_memory_error():
    oversized_program = [0] * (RAM_LEN + 1)
    vm = VirtualMachine()
    try:
        vm.initialize(oversized_program)
    except AssertionError:
        pass


def test_unknown_instruction():
    vm = VirtualMachine()
    lines = ['00000c'] 
    unknown_instruction_program = [int(ln, 16) for ln in lines if ln]
    vm.initialize(unknown_instruction_program)
    op_code = vm.fetch()[0]
    valid_op_codes = {details['code'] for details in OPS.values()}
    try:
        if op_code not in valid_op_codes:
            assert False, f"Unknown instruction code"
    except AssertionError:
        pass  

def test_output_input_file_1():
    asm = Assembler()
    with open('addTwoNum.as','r') as f:
        lines_as = f.read().splitlines()
    with open('addTwoNum_manCalc.mx','r') as m:
        lines_mx = m.read().splitlines()
    expected_output = lines_mx
    print(expected_output)
    real_output = asm.assemble(lines_as)
    print(real_output)
    assert real_output == expected_output


def test_output_input_file_2():
    asm = Assembler()
    with open('loop.as','r') as f:
        lines_as = f.read().splitlines()
    with open('loop_manCalc.mx','r') as m:
        lines_mx = m.read().splitlines()
    expected_output = lines_mx
    print(expected_output)
    real_output = asm.assemble(lines_as)
    print(real_output)
    assert real_output == expected_output


def test_output_input_file_3():
    asm = Assembler()
    with open('temp.as','r') as f:
        lines_as = f.read().splitlines()
    with open('temp_manCalc.mx','r') as m:
        lines_mx = m.read().splitlines()
    expected_output = lines_mx
    print(expected_output)
    real_output = asm.assemble(lines_as)
    print(real_output)
    assert real_output == expected_output

# Test case for VirtualMachine - tested operations are: ldc, add, prr, hlt
def test_output_input_file_vm1():
    vm = VirtualMachine()
    asm = Assembler()

    with open('temp.as','r') as f:
        lines_as = f.read().splitlines()
    lines_mx = asm.assemble(lines_as)
    expected_output = []
    for num in lines_mx: 
        expected_output.append(int(num,16))
    program = [int(ln, 16) for ln in lines_mx if ln]
    vm.initialize(program)
    for num in vm.ram:
        index_not_used_ram = vm.ram.index(0)
    real_output = vm.ram[:index_not_used_ram]
    print(real_output)
    print(expected_output)
    assert real_output == expected_output



# Test case for VirtualMachine - tested operations are: ldc, prr, sub, bne, hlt
def test_output_input_file_vm2():
    vm = VirtualMachine()
    asm = Assembler()

    with open('loop.as','r') as f:
        lines_as = f.read().splitlines()
    lines_mx = asm.assemble(lines_as)
    expected_output = []
    for num in lines_mx: 
        expected_output.append(int(num,16))
    program = [int(ln, 16) for ln in lines_mx if ln]
    vm.initialize(program)
    for num in vm.ram:
        index_not_used_ram = vm.ram.index(0)
    real_output = vm.ram[:index_not_used_ram]
    print(real_output)
    print(expected_output)
    assert real_output == expected_output


# Test case for VirtualMachine - tested operations are: ldc, ldr, cpy, sub, str, beq, prm, hlt
def test_output_input_file_vm3():
    vm = VirtualMachine()
    asm = Assembler()

    with open('temp.as','r') as f:
        lines_as = f.read().splitlines()
    lines_mx = asm.assemble(lines_as)
    expected_output = []
    for num in lines_mx: 
        expected_output.append(int(num,16))
    program = [int(ln, 16) for ln in lines_mx if ln]
    vm.initialize(program)
    for num in vm.ram:
        index_not_used_ram = vm.ram.index(0)
    real_output = vm.ram[:index_not_used_ram]
    print(real_output)
    print(expected_output)
    assert real_output == expected_output



# Measure and report the test coverage in % for the above tests - call in the terminal
# coverage run -m pytest arg1 arg2 arg3
# coverage report -m
# coverage html

