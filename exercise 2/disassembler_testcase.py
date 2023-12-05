import pytest 
from disassembler import Dissassembler
import os 

def test_successful_translation():
    # with open('test.mx','w') as f:
    test_case = ['000002','030102','00000a','010202','020006','010204','000207','020209','000001']
    expected = ['ldc R0 0','ldc R1 3','L001:','prr R0','ldc R2 1','add R0 R2','cpy R2 R1','sub R2 R0','bne R2 @L001','hlt']
    dissassembler = Dissassembler()
    actual = dissassembler.dissassembler(test_case)
    assert expected == actual

def test_duplicated_code_error():
    test_case = ['000002','030102','00000a','010202','020006','010204','000207','020209','020209','000001']
    dissassembler = Dissassembler()
    with pytest.raises(AssertionError):
        dissassembler.dissassembler(test_case)


def test_argument1_not_zero():
    test_case = ['000002','030102','00000a','010202','020006','010204','000207','020209','010001']
    dissassembler = Dissassembler()
    with pytest.raises(AssertionError):
        dissassembler.dissassembler(test_case)

def test_argument2_not_zero():
    test_case = ['000002','030102','01000a','010202','020006','010204','000207','020209','000001']
    dissassembler = Dissassembler()
    with pytest.raises(AssertionError):
        dissassembler.dissassembler(test_case)

def test_combine_error():
    test_case = ['000002','00030102','00000a','010202','020006','010204','000207','020209','000001']
    dissassembler = Dissassembler()
    with pytest.raises(AssertionError):
        dissassembler.dissassembler(test_case)

def test_illegal_register():
    test_case = ['000902','030102','00000a','010202','020006','010204','000207','020209','000001']
    dissassembler = Dissassembler()
    with pytest.raises(AssertionError):
        dissassembler.dissassembler(test_case)