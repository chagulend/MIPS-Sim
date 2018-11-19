from cpu_element import CPU_element


class Instruction_pointer(CPU_element):
    def write_outputs(self):
        input_name = self.input_names[0]
        result = self.output_names[0]
        self.outputs[result] = self.inputs[input_name]


class Adder(CPU_element):
    def write_outputs(self):
        result = self.output_names[0]
        self.outputs[result] = sum(self.inputs.values()) & 0xffffffff


class Mux(CPU_element):
    def write_outputs(self):
        control = self.inputs[self.input_names[0]]
        result = self.output_names[0]
        if control:
            self.outputs[result] = self.inputs[self.input_names[2]]
        else:
            self.outputs[result] = self.inputs[self.input_names[1]]


class Memory(CPU_element):
    pass
