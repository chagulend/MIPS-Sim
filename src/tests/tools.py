def set_signals(source, target, signals, values):
    for name, value in zip(signals, values):
        source.outputs[name] = value
    target.read_inputs()
    target.write_outputs()
