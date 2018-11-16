import pytest
from cpu_element import CPU_element
from mux import Mux


signals = ["control", "one", "two"]
result = "result"


class Test_Mux:
    source = CPU_element([], signals)
    mux = Mux(signals, [result])
    assert isinstance(mux, CPU_element)
    mux.connect([source])

    def test_write_output(self):
        assert self.mux.outputs[result] == 0
