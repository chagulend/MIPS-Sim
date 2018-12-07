from cpu_element import CPU_element
from elements import Adder
from tests.tools import set_signals


signals = ["a", "b"]
result = "result"


def test_write_outputs():
    source = CPU_element([], signals)
    adder = Adder(signals, [result])
    assert isinstance(adder, CPU_element)
    adder.connect([source])
    a = 42
    b = 8
    set_signals(source, adder, signals, [a, b])
    assert adder.outputs[result] == a + b
    a = 2**32 - 1
    set_signals(source, adder, signals, [a, b])
    assert adder.outputs[result] == (a + b) & a
