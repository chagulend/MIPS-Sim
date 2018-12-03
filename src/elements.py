from cpu_element import CPU_element


class Instruction_pointer(CPU_element):
    def write_outputs(self):
        input_name = self.input_names[0]
        result = self.output_names[0]
        self.outputs[result] = self.inputs[input_name]

    def status(self):
        """ Returns the current instruction address as a printable string."""
        result = self.output_names[0]
        outputs = ["---Instruction pointer---"]
        outputs.append("Hex value: 0x{:08x}".format(self.outputs[result]))
        outputs.append("Value: {}".format(self.outputs[result]))
        return "\n".join(outputs)


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


class Constant(CPU_element):
    def __init__(self, output_name, value):
        if not isinstance(value, int):
            raise TypeError("value should be a int.")
        super().__init__([], [output_name])
        self.value = value

    def write_outputs(self):
        result = self.output_names[0]
        self.outputs[result] = self.value
