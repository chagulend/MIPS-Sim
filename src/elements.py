from cpu_element import CPU_element


class Instruction_pointer(CPU_element):
    def write_outputs(self):
        input_name = self.input_names[0]
        result = self.output_names[0]
        self.outputs[result] = self.inputs[input_name]

    def status(self):
        """ Returns the current instruction address as a printable string."""
        address = self.outputs[self.output_names[0]]
        outputs = ["---Instruction pointer---"]
        outputs.append("Hex value: 0x{:08x}".format(address))
        outputs.append("Value: {}".format(address))
        return "\n".join(outputs)


class Adder(CPU_element):
    """
    Adder element.
    """
    def write_outputs(self):
        """
        Sums all inputs, masking output such that the result is 32 bit.
        """
        result = self.output_names[0]
        mask = 0xffffffff
        self.outputs[result] = sum(self.inputs.values()) & mask


class Mux(CPU_element):
    def write_outputs(self):
        control = self.inputs[self.input_names[0]]
        result = self.output_names[0]
        if control == 0:
            self.outputs[result] = self.inputs[self.input_names[1]]
        else:
            self.outputs[result] = self.inputs[self.input_names[2]]


class Constant(CPU_element):
    """
    Element with constant output. Intended as a demo component.
    """
    def __init__(self, output_name, value):
        if not isinstance(value, int):
            raise TypeError("value should be a int.")
        super().__init__([], [output_name])
        self.value = value

    def write_outputs(self):
        """
        Set output to initial value. Implemented to allow
        write_outputs to be called without raising parent
        class exception.
        """
        result = self.output_names[0]
        self.outputs[result] = self.value
