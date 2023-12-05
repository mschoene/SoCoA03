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

# test the format --: example hlt
def test_invalid_instruction_format_hlt():
    asm = Assembler()
    lines = ['hlt R1 R1']  # invalid format

    # Expecting an AssertionError due to incorrect instruction format
    with pytest.raises(AssertionError):
        asm.assemble(lines)

# test the format rv: example ldc
def test_instruction_not_found_error_rv1():
    asm = Assembler()
    lines = ['ldc R1 R1']  # invalid format

    # Expecting an AssertionError due to incorrect instruction format
    with pytest.raises(ValueError):
        asm.assemble(lines)

# test the format rv: example ldc, invalid register name
def test_instruction_not_found_error_rv2():
    asm = Assembler()
    lines = ['ldc r1 2']  # invalid format

    # Expecting an AssertionError due to incorrect instruction format
    with pytest.raises(AssertionError):
        asm.assemble(lines)


# test the format rr: example ldr, excedeeding register
def test_instruction_not_found_error_rr1():
    asm = Assembler()
    lines = ['ldr R9 R1']  # invalid format

    # Expecting an AssertionError due to incorrect instruction format
    with pytest.raises(AssertionError):
        asm.assemble(lines)

# test the format rr: example ldr, invalid argument
def test_instruction_not_found_error_rr2():
    asm = Assembler()
    lines = ['ldr R1 1']  # invalid format

    # Expecting an AssertionError due to incorrect instruction format
    with pytest.raises(AssertionError):
        asm.assemble(lines)


# test the format r-: example prr, invalid argument
def test_instruction_not_found_error_r():
    asm = Assembler()
    lines = ['prr R1 R2']  # invalid format

    # Expecting an AssertionError due to incorrect instruction format
    with pytest.raises(AssertionError):
        asm.assemble(lines)

# Measure and report the test coverage in % for the above tests - call in the terminal
# coverage run -m pytest arg1 arg2 arg3
# coverage report -m
# coverage html


