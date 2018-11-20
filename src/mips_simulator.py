#!/usr/bin/env python3
from cpu_element import CPU_element
from elements import (Adder, Mux, Register_file, Instruction_pointer,
                      Constant)
from memory import Data_memory, Instruction_memory


class MIPS_simulator:
    def __init__(self):
        self.ticks = 0
        elements = []
        self.ip = Instruction_pointer(["Ins_incr"], ["Ins_out"])
        elements.append(self.ip)
        elements.append(Constant(4, "Constant"))
        elements.append(Constant(1, "Control"))
        elements.append(Adder(["Constant", "Ins_out"], ["Ins_incr"]))
        elements.append(Mux(["Control", "Ins_out", "Ins_incr"], ["Result"]))
        self.elements = elements
        self._connect_elements()

    def _connect_elements(self):
        for element in self.elements:
            element.connect(self.elements)

    def tick(self):
        for element in self.elements:
            element.read_inputs()
            element.write_outputs()
        self.ticks += 1

    def status(self):
        outputs = ["Total ticks: {}".format(self.ticks)]
        outputs.append(self.ip.status())
        outputs.append("Result: {}"
                       .format(self.elements[-1].outputs["Result"]))
        return "\n".join(outputs)


if __name__ == "__main__":
    simulator = MIPS_simulator()
    for i in range(10):
        simulator.tick()
        print(simulator.status())
    
