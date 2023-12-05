# SoCoA03
Software construction assignment 3

## Unit Testing 
Three assembly files (addTwoNum.as, loop.as, temp.as) were created, covering all instructions in the OPS dictionary.
These assembly files have been manually translated into machine code, resulting in corresponding .mx files (addTwoNum_manCalc.mx, loop_manCalc.mx, temp_manCalc.mx).

### Test the Assembler 
1. test_output_input_file_1(): Validates the assembly of addTwoNum.as by comparing the assembler's output to the expected machine code in addTwoNum_manCalc.mx.
2. test_output_input_file_2(): Tests the assembly of loop.as, with results compared against loop_manCalc.mx.
3. test_output_input_file_3(): Checks the assembly of temp.as against the expected machine code in temp_manCalc.mx.

### Test the Virtual Machine
1. test_output_input_file_vm1(): Validates the execution of the program in `temp.as`. It checks the Virtual Machine's ability to process assembly instructions, convert them to machine code using the `Assembler`, and then execute them. The expected output is determined by the initial part of the VM's RAM before encountering the first zero value.

2. test_output_input_file_vm2(): Tests the functionality of the Virtual Machine with the program in `loop.as`. This test focuses on the VM's handling of looping constructs and other operations defined in the file. The test compares the RAM state of the VM before the first zero value against an expected output.

3. test_output_input_file_vm3(): Checks the execution of the assembly program in `temp.as` using the Virtual Machine. This test assesses the VM's ability to handle a variety of operations including `ldc`, `ldr`, `cpy`, `sub`, `str`, `beq`, `prm`, and `hlt`. The expected output is determined similarly to the other tests, based on the VM's RAM state before the first zero value.


#### Usage Pytest
In the folder exercise 1 run:
```pytest vm_testcase.py```


### Test coverage

Need to first install it if not having the packege: pip install pytest coverage

Run the tests with coverage: 

```coverage run -m pytest vm_testcase.py```

for the coverage report:

For a terminal report: ```coverage report```
  
For a detailed HTML report: ```coverage html```

The HTML report will be in the `htmlcov` directory, open `htmlcov/index.html` in the browser to view it.

## Disassembler
Disassembler converts virtual machine (VM) instructions back into assembly code.

#### Usage
```python disassembler.py example_input.mx example_output.as``` 


## Debugger

### Starting the debugger
To start the debugging program run:
```python .\debugger\vm_break.py .\debugger\count_up.mx```

The following commands can be entered:
 "dis", "ip", "memory", "quit", "run", "step", "break", "clear", "watch".
Use any length of starting characters to trigger the commmand. E.g. for "memory":  m, me, mem, ..., memory.
### Show memory
Show the memory with the "memory" command. Use it with 1-2 addresses to show the value at said address or the values between the range of those addresses, respectively. E.g.:

```
me 
m 1 
m 1 2 
```

### Breakpoint

To set or remove a breakpoint use the "break" and "clear" commands respectively. Provide an address to either of them for the action to affect that specific address. E.g.:
```
m 5
b 5 
m 5
c 5
m 5
```
This will show the memory held at the 5th address (010204). Then a break point is set at that address. Which is shown in the memory (00000f). Then it is removed again and the memory is again what it was in the beginning (010204).


### Watchpoint

To add a watchpoint at an address write:

```w 5```
