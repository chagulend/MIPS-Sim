import pytest
from cpu_element import CPU_element

source = "source"
result = "result"


class Test_CPU_element:
    def test_init(self):
        with pytest.raises(TypeError):
            CPU_element()
            CPU_element(source)
            CPU_element(source, result)
            CPU_element([1], [2])
        cpu = CPU_element([source], [result])
        assert source in cpu.inputs
        assert source not in cpu.outputs
        assert result in cpu.outputs
        assert result not in cpu.inputs

    def test_connect(self):
        a = CPU_element([], [result])
        b = CPU_element([result], [])
        with pytest.raises(TypeError):
            b.connect(a)
            b.connect(5)
            b.connect([5])
        b.connect([a])
        assert b.input_sources[result] == a
        with pytest.raises(KeyError):
            b.input_sources[source]
            b.connect([CPU_element([], [result])])

    def test_read_input(self):
        a = CPU_element([], [result])
        b = CPU_element([result], [])
        i = 42
        b.connect([a])
        a.outputs[result] = i
        b.read_inputs()
        assert b.inputs[result] == i

    def test_write_output(self):
        with pytest.raises(NotImplementedError):
            CPU_element([], []).write_output()
