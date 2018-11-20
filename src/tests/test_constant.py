import pytest
from cpu_element import CPU_element
from elements import Constant


result = "result"
value = 4


class Test_Constant:
    def test_init(self):
        with pytest.raises(TypeError):
            Constant(2.2, result)
        with pytest.raises(TypeError):
            Constant(value, 8)

    def test_write_outputs(self):
        a = Constant(value, result)
        a.write_outputs()
        assert a.outputs[result] == value

    def test_connect(self):
        with pytest.raises(TypeError):
            a = Constant(value, result)
            a.connect(CPU_element([], []))

    def test_read_inputs(self):
        a = Constant(value, result)
        a.read_inputs()
