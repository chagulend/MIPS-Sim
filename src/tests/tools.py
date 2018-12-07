def set_signals(source, target, signals, values):
    """ Sets source output signals to values and calls
    read_inputs and write outputs on target."""
    for name, value in zip(signals, values):
        source.outputs[name] = value
    target.read_inputs()
    target.write_outputs()
