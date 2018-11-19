from cpu_element import CPU_element
from adder import Adder
from tests.tools import set_signals


sources = ["a", "b"]
result = "result"


class Test_Adder:
    a = CPU_element([], sources)
    b = Adder(sources, [result])
    assert isinstance(b, CPU_element)
    b.connect([a])

    def test_write_outputs(self):
        a = 42
        b = 8
        set_signals(self.a, self.b, sources, [a, b])
        assert self.b.outputs[result] == a + b
        a = 2**32 - 1
        set_signals(self.a, self.b, sources, [a, b])
        assert self.b.outputs[result] == (a + b) & a
