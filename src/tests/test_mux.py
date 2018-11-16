import pytest
from cpu_element import CPU_element
from mux import Mux


signals = ["control", "zero", "one"]
result = "result"

def set_signals(source, target, signals, values):
    for name, value in zip(signals, values):
        source.outputs[name] = value
    target.read_inputs()
    target.write_outputs()


class Test_Mux:
    source = CPU_element([], signals)
    mux = Mux(signals, [result])
    assert isinstance(mux, CPU_element)
    mux.connect([source])

    def test_write_outputs(self):
        zero = 55
        one = 44
        set_signals(self.source, self.mux, signals, [True, zero, one])
        assert self.mux.outputs[result] == one
        set_signals(self.source, self.mux, signals, [False, zero, one])
        assert self.mux.outputs[result] == zero
