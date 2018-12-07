import pytest
from cpu_element import CPU_element
from elements import Mux
from tests.tools import set_signals


signals = ["control", "zero", "one"]
result = "result"


def test_write_outputs():
    source = CPU_element([], signals)
    mux = Mux(signals, [result])
    assert isinstance(mux, CPU_element)
    mux.connect([source])
    zero = 55
    one = 44
    set_signals(source, mux, signals, [True, zero, one])
    assert mux.outputs[result] == one
    set_signals(source, mux, signals, [False, zero, one])
    assert mux.outputs[result] == zero
