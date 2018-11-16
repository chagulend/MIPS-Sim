class CPU_element:
    def __init__(self, input_names, output_names):
        self.inputs = self._init_verify(input_names, "inputs")
        self.outputs = self._init_verify(output_names, "outputs")
        self.input_names = input_names
        self.output_names = output_names
        self.input_sources = {}

    def _init_verify(self, names, type):
        if not isinstance(names, list):
            raise TypeError("{}_names must be a list.".format(type))
        for name in names:
            if not isinstance(name, str):
                raise TypeError("A {} name must be a string.".format(type))
        return {name:0 for name in names}

    def connect(self, inputs):
        """ Connects a cpu element to its inputs."""
        if not isinstance(inputs, list):
            raise TypeError("inputs must be a list.")
        for element in inputs:
            if not isinstance(element, CPU_element):
                raise TypeError("Inputs list should only contain instances"
                                + " of CPU_element.")
            for output in element.outputs:
                source = self.input_sources.setdefault(output, element)
                if source != element:
                    raise KeyError("Duplicace input name detected;"
                                   + " got {} from {}".format(output, element)
                                   + " Has: {} from {}."
                                   .format(source, self.input_sources[source]))

    def read_inputs(self):
        """ Reads the inputs of the cpu element. Raises a KeyError if
        the element misses a input source."""
        for name in self.inputs:
            element = self.input_sources[name]
            value = 0
            try:
                value = element.outputs[name]
                self.inputs[name] = value
            except KeyError:
                pass
            if not isinstance(value, int):
                raise TypeError("Input should only use integers."
                                + " Got {} from {}.".format(value, element))

    def write_outputs(self):
        raise NotImplementedError(
            "write_output must be implemented by CPU Element:", self)
