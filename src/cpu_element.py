class CPU_element:
    """ Intended for subclassing. Defines the methods:
    __init__, connect, read_inputs and write_outputs.
    """
    def __init__(self, input_names, output_names):
        self.inputs = dict.fromkeys(input_names, 0)
        self.outputs = dict.fromkeys(output_names, 0)
        self.input_names = input_names
        self.output_names = output_names
        self.input_sources = dict()

    def connect(self, inputs):
        """ Connects a element to its inputs."""
        if not isinstance(inputs, list):
            raise TypeError("inputs must be a list.")
        input_names = set(self.input_names)
        for element in inputs:
            if not isinstance(element, CPU_element):
                raise TypeError("Inputs list should only contain instances"
                                + " of CPU_element.")
            if element == self:
                continue
            sources = input_names.intersection(element.outputs)
            self.input_sources.update({key:element for key in sources})
        missing = input_names.difference(self.input_sources)
        if missing != set():
            raise ValueError(self, "was not connected fully, missing", missing)

    def read_inputs(self):
        """ Updates the inputs dictionary."""
        for name, element in self.input_sources.items():
            value = element.outputs.get(name)
            if value == None:
                continue
            if not isinstance(value, int):
                raise TypeError("Input should only use integers. "
                                + "Got {} from {}.".format(value, element))
            self.inputs[name] = value

    def write_outputs(self):
        """ Updates outputs dictionary. Should be implemented by subclasses."""
        raise NotImplementedError(
            "write_outputs must be implemented by:", self)
