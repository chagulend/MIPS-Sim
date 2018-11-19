from cpu_element import CPU_element


class Memory(CPU_element):
    def __init__(self, file_name, input_names, output_names):
        super().__init__(input_names, output_names)
        if not isinstance(file_name, str):
            raise TypeError("file_name must be a string.")
        self.memory = self._initialize_memory(file_name)        

    def status(self):
        """ Returns the memory as a printable string."""
        outputs = ["---Memory---"]
        for address, value in self.memory.items():
            outputs.append("Address: {} \t Hex value: 0x{:08x}."
                           .format(address, value))
        return "\n".join(outputs)

    def _initialize_memory(self, file_name):
        raise NotImplementedError


class Data_memory(Memory):
    pass


class Instruction_memory(Memory):
    pass
