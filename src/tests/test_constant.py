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
            Constant(value, result)
        a = Constant(result, value)
        assert a.inputs == {}
        assert a.input_names == []

    def test_write_outputs(self):
        a = Constant(result, value)
        a.write_outputs()
        assert a.outputs[result] == value

    def test_connect(self):
        a = Constant(result, value)
        a.connect([a])
        assert a.input_sources == dict()

    def test_read_inputs(self):
        a = Constant(result, value)
        inputs = a.inputs.copy()
        a.read_inputs()
        assert inputs == a.inputs
        assert a.inputs == dict()
