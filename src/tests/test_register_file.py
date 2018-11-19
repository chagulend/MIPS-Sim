from cpu_element import CPU_element
from elements import Register_file


class Test_Register_file:
    def test_initial_state(self):
        assert Register_file([], []).registers == {i:0 for i in range(32)}

    def test_write_outputs(self):
        raise NotImplementedError
        
