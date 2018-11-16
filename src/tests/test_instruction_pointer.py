from cpu_element import CPU_element
from instruction_pointer import Instruction_pointer


signals = "input"
result = "result"


class Test_Instruction_pointer:
    source = CPU_element([], [signals])
    ip = Instruction_pointer([signals], [result])
    assert isinstance(ip, CPU_element)
    ip.connect(source)

    def test_write_output(self):
        pass
