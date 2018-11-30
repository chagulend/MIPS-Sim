from cpu_element import CPU_element
from register_file import Register_file


class Test_Register_file:
    def test_initial_state(self):
        a = Register_file([], [])
        assert a.registers == {i:0 for i in range(32)}
        
