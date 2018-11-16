import pytest
from cpu_element import CPU_element
from mux import Mux


signals = ["control", "one", "two"]
result = "result"

def set_signals(source, target, signals, values):
    for name, value in zip(signals, values):
        source.outputs[name] = value
    target.read_inputs()


class Test_Mux:
    source = CPU_element([], signals)
    mux = Mux(signals, [result])
    assert isinstance(mux, CPU_element)
    mux.connect([source])

    def test_write_output(self):
        zero = 55
        one = 44
        control = True
        values = [control, zero, one]
        set_signals(self.source, self.mux, signals, values)
        assert self.mux.outputs[result] == one
        control = False
        set_signals(self.source, self.mux, signals, values)
        assert self.mux.outputs[result] == zero
