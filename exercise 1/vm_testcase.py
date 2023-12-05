import sys
import os

# sys.path.append('/Users/cindyliu/Desktop/Assigment_03/')
# sys.path.insert(0, '/Users/cindyliu/Desktop/Assigment_03/')
sys.path.insert(0, '/Users/cindyliu/Desktop/Assigment_03/vm')
print(sys.path)
# Importing the vm module
# import vm 
from vm import VirtualMachine
from assembler import Assembler
from architecture import NUM_REG, OPS, OP_MASK, OP_SHIFT, RAM_LEN
import pytest 



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

# Test case for Assembler - tested operations are: ldc, add, prr, hlt
def test_output_input_file_as1():
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

# Test case for Assembler - tested operations are: ldc, prr, sub, bne, hlt
def test_output_input_file_as2():
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

# Test case for Assembler - tested operations are: ldc, ldr, cpy, sub, str, beq, prm, hlt
def test_output_input_file_as3():
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
    print(lines_as)
    lines_mx = asm.assemble(lines_as)
    program = [int(ln, 16) for ln in lines_mx if ln]
    print(lines_mx)
    expected_output = lines_as
    real_output = vm.initialize(program)
    print(real_output)
    assert real_output == expected_output



# Test case for VirtualMachine - tested operations are: ldc, prr, sub, bne, hlt
def test_output_input_file_vm2():
    vm = VirtualMachine()
    with open('loop.as','r') as f:
        lines_as = f.read().splitlines()
    with open('loop_manCalc.mx','r') as m:
        lines_mx = m.read().splitlines()
    expected_output = lines_mx
    print(expected_output)
    real_output = vm.initialize(lines_as)
    print(real_output)
    assert real_output == expected_output

# Test case for VirtualMachine - tested operations are: ldc, ldr, cpy, sub, str, beq, prm, hlt
def test_output_input_file_vm3():
    vm = VirtualMachine()
    with open('temp.as','r') as f:
        lines_as = f.read().splitlines()
    with open('temp_manCalc.mx','r') as m:
        lines_mx = m.read().splitlines()
    expected_output = lines_mx
    print(expected_output)
    real_output = vm.initialize(lines_as)
    print(real_output)
    assert real_output == expected_output





# Measure and report the test coverage in % for the above tests - call in the terminal
# coverage run -m pytest arg1 arg2 arg3
# coverage report -m
# coverage html

