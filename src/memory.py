from cpu_element import CPU_element


class Memory(CPU_element):
    def __init__(self, inputs, outputs):
        self.memory = {}

    def status(self):
        """ Returns the memory as a printable string."""
        outputs = ["---Memory---"]
        for address, value in self.memory.items():
            outputs.append("Address: {} \t Hex value: 0x{:08x}."
                           .format(address, value))
        return "\n".join(outputs)

    def initialize_memory(self, file_name):
        if not isinstance(file_name, str):
            raise TypeError("file_name must be a string.")


class Data_memory(Memory):
    pass


class Instruction_memory(Memory):
    pass
