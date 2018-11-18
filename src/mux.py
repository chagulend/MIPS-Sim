from cpu_element import CPU_element


class Mux(CPU_element):
    def write_outputs(self):
        control = self.inputs[self.input_names[0]]
        result = self.output_names[0]
        if control:
            self.outputs[result] = self.inputs[self.input_names[2]]
        else:
            self.outputs[result] = self.inputs[self.input_names[1]]
