import pytest
from cpu_element import CPU_element
from mux import Mux
from tests.tools import set_signals


signals = ["control", "zero", "one"]
result = "result"


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
