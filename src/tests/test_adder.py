from cpu_element import CPU_element
from elements import Adder
from tests.tools import set_signals


sources = ["a", "b"]
result = "result"


def test_write_outputs(self):
    source = CPU_element([], sources)
    adder = Adder(sources, [result])
    assert isinstance(adder, CPU_element)
    adder.connect([source])
    a = 42
    b = 8
    set_signals(source, adder, sources, [a, b])
    assert self.adder.outputs[result] == a + b
    a = 2**32 - 1
    set_signals(source, adder, sources, [a, b])
    assert self.adder.outputs[result] == (a + b) & a
