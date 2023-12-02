import sys
import os

# sys.path.append('/Users/cindyliu/Desktop/Assigment_03/')
# sys.path.insert(0, '/Users/cindyliu/Desktop/Assigment_03/')
sys.path.insert(0, '/Users/cindyliu/Desktop/Assigment_03/vm')
print(sys.path)
# Importing the vm module
# import vm 
from vm import VirtualMachine
from architecture import NUM_REG, OPS, OP_MASK, OP_SHIFT, RAM_LEN
import pytest 



def test_out_of_memory_error():
    oversized_program = [0] * (RAM_LEN + 1)
    vm = VirtualMachine()
    with pytest.raises(AssertionError): 
        vm.initialize(oversized_program)


def test_instruction_not_found1_error():
    # add R1 08 <-- Wrong instruction, correct format should be add r r: add R0 R1
    errors_instrucion = [14,2,2]
    vm = VirtualMachine()
    with pytest.raises(AssertionError): 
        vm.initialize(errors_instrucion)
        vm.run()

# Measure and report the test coverage in % for the above tests - call in the terminal
# coverage run -m pytest arg1 arg2 arg3
# coverage report -m
# coverage html




