from cpu_element import CPU_element
from elements import Instruction_pointer
from tests.tools import set_signals

signals = "input"
result = "result"


class Test_Instruction_pointer:
    source = CPU_element([], [signals])
    ip = Instruction_pointer([signals], [result])
    assert isinstance(ip, CPU_element)
    ip.connect([source])

    def test_write_output(self):
        value = 55
        set_signals(self.source, self.ip, [signals], [value])
        assert self.ip.outputs[result] == value
