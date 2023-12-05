# SoCoA03
Software construction assignment 3

## Unit Testing 

### Test the Assembler 
Created three files which contain the assembly code, the three files covers all the 11 instructions in OPS dictionary. Then we manually trasnlated the assembly code into machine code. 
To test the assembler, we have created three tests which get the 



### Test coverage

Need to first install it if not having the packege: pip install pytest coverage

Run the tests with coverage: coverage run -m pytest + file.py

for the coverage report:

    - For a terminal report: coverage report
  
    - For a detailed HTML report: coverage html

The HTML report will be in the `htmlcov` directory, open `htmlcov/index.html` in the browser to view it.



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
