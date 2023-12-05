import sys

from architecture import OPS, VMState
from vm_extend import VirtualMachineExtend


class VirtualMachineBreak(VirtualMachineExtend):
    # [init]
    def __init__(self):
        super().__init__()
        self.breaks = {}
        self.watchpoints = {}
        self.handlers |= {
            "break": self._do_add_breakpoint,
            "clear": self._do_clear_breakpoint,
            "watch": self._do_add_watchpoint,
        }
    # [/init]

    # [show]
    def show(self):
        super().show()
        # additional printing for breaks
        if self.breaks:
            self.write("-" * 6)
            for key, instruction in self.breaks.items():
                self.write(f"{key:06x}: {self.disassemble(key, instruction)}")

        #special printing for watchpoints
        if self.watchpoints:
            self.write("-" * 6)
            for key, value in self.watchpoints.items():
                self.write(f"{key:06x}: Watchpoint ({value})")
    # [/show]

    # [run]
    def run(self):
        self.state = VMState.STEPPING
        while self.state != VMState.FINISHED:
            instruction = self.ram[self.ip]
            op, arg0, arg1 = self.decode(instruction)

            if op == OPS["brk"]["code"]:
                original = self.breaks[self.ip]
                op, arg0, arg1 = self.decode(original)
                self.interact(self.ip)
                self.ip += 1
                self.execute(op, arg0, arg1)

            else:
                if self.state == VMState.STEPPING:
                    self.interact(self.ip)
                
                if self.ip in self.watchpoints:
                    if self.ram[self.ip] != self.watchpoints[self.ip]:
                        print(f"Watchpoint at address {self.ip:06x}")
                        self.interact(self.ip)  # i.a. when watchpoint is met
                        self.state = VMState.FINISHED

                self.ip += 1
                self.execute(op, arg0, arg1)
    # [/run]

    # [add watchpoint]
    def _do_add_watchpoint(self, addr, set_addr):

        if(set_addr):
            addr = int( set_addr[0][0])
        #check if add is already in watchpoints
        if addr in self.watchpoints:
            return False 
        
        self.watchpoints[addr] = self.ram[addr]
        return True

    # [/add watchpoint]

    # [add]
    def _do_add_breakpoint(self, addr, *set_addr):
        
        #if user gives specific addr set brkpnt at that add instead of current ip
        if(set_addr):
            addr = int( set_addr[0][0])
        if self.ram[addr] == OPS["brk"]["code"]:
            return
        self.breaks[addr] = self.ram[addr]
        self.ram[addr] = OPS["brk"]["code"]
        return True
    # [/add]

    # [clear]
    def _do_clear_breakpoint(self, addr, *set_addr):
        
        #if user gives specific addr clear brkpnt at that add instead of current ip
        if(set_addr):
            addr = int( set_addr[0][0])

        if self.ram[addr] != OPS["brk"]["code"]:
            return
        self.ram[addr] = self.breaks[addr]
        del self.breaks[addr]
        return True
    # [/clear]


if __name__ == "__main__":
    VirtualMachineBreak.main()
