import sys

from architecture import VMState
from vm_step import VirtualMachineStep
from vm_base import COLUMNS, DIGITS


class VirtualMachineExtend(VirtualMachineStep):
    # [init]
    def __init__(self, reader=input, writer=sys.stdout):
        super().__init__(reader, writer)
        self.handlers = {
            "dis": self._do_disassemble,
            "ip": self._do_ip,
            "memory": self._do_memory,
            "quit": self._do_quit,
            "run": self._do_run,
            "step": self._do_step,
        }
    # [/init]

    # [interact]
    def interact(self, addr):
        prompt = "".join(sorted({key[0] for key in self.handlers}))
        interacting = True
        while interacting:
            try:
                command = self.read(f"{addr:06x} [{prompt}]> ")
                split_commands = command.split(" ")
                command = split_commands[0]
                com_li = [com for com in self.handlers.keys() if com.startswith(command)] # list of all commands starting with the prompt
                # if a command was entered, take the first match
                if len(com_li)>0:
                    command = com_li[0]
                if not command:
                    continue
                elif command not in self.handlers:
                    self.write(f"Unknown command {command}")
                else:
                    if len(split_commands)>1:
                        interacting = self.handlers[command](self.ip, split_commands[1:])
                    else:
                        interacting = self.handlers[command](self.ip)
            except EOFError:
                self.state = VMState.FINISHED
                interacting = False
    # [/interact]

    def _do_disassemble(self, addr):
        self.write(self.disassemble(addr, self.ram[addr]))
        return True

    def _do_ip(self, addr):
        self.write(f"{self.ip:06x}")
        return True

    # [memory]
    def _do_memory(self, *args):

        if args:
            addrs = args[1:] #get address range if given 
            
        if addrs:
            assert len(addrs[0]) <=2, "Too many memory addresses given!"
            
            if len(addrs[0]) ==1: # show one single addr
                base = int(addrs[0][0])
                self.write( f" {self.ram[base ]:06x}")
                return True
            elif len(addrs[0])==2: # show addr range
                base, top =  int(addrs[0][0]), int(addrs[0][1])
                output = ""   
                for i in range(base, top+1): # +1 to include upper addess bound
                    output += f" {self.ram[i]:06x}"
                self.write(output)
                return True

        # if no address specified show all from super
        self.show()
        return True
    # [/memory]

    def _do_quit(self, addr):
        self.state = VMState.FINISHED
        return False

    def _do_run(self, addr):
        self.state = VMState.RUNNING
        return False

    # [step]
    def _do_step(self, addr):
        self.state = VMState.STEPPING
        return False
    # [/step]


if __name__ == "__main__":
    VirtualMachineExtend.main()
