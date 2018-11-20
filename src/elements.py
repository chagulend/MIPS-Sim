from cpu_element import CPU_element


class Instruction_pointer(CPU_element):
    def write_outputs(self):
        input_name = self.input_names[0]
        result = self.output_names[0]
        self.outputs[result] = self.inputs[input_name]

    def status(self):
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
    def __init__(self, value, output_name):
        if not isinstance(value, int):
            raise TypeError("value should be a int.")
        if not isinstance(output_name, str):
            raise TypeError("output_name should be a string.")
        super().__init__([], [output_name])
        self.value = value

    def write_outputs(self):
        result = self.output_names[0]
        self.outputs[result] = self.value


class Register_file(CPU_element):
    registers = {i:0 for i in range(32)}

    def status(self):
        """ Returns the registry as a printable string."""
        register_names = ["$zero", "$at", "$v0", "$v1", "$a0",
                          "$a1", "$a2", "$a3", "$t0", "$t1",
                          "$t2", "$t3", "$t4", "$t5", "$t6",
                          "$t7", "$s0", "$s1", "$s2", "$s3",
                          "$s4", "$s5", "$s6", "$s7", "$t8",
                          "$t9", "$k0", "$k1", "$gp", "$sp",
                          "$fp", "$ra"]
        outputs = ["---Register file---"]
        for i, name in enumerate(register_names):
            value = self.registers[i]
            outputs.append("Name: {} \t Hex value: 0x{:08x} \t Value: {}."
                           .format(name, value, value))
        return "\n".join(outputs)
