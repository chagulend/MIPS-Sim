import pytest
from cpu_element import CPU_element


source = "source"
result = "result"


class Test_CPU_element:
    def test_init(self):
        with pytest.raises(TypeError):
            CPU_element()
        with pytest.raises(TypeError):
            CPU_element(source, result)
        with pytest.raises(TypeError):
            CPU_element([1], [2])
        cpu = CPU_element([source], [result])
        assert source in cpu.inputs
        assert source not in cpu.outputs
        assert result in cpu.outputs
        assert result not in cpu.inputs

    def test_connect(self):
        a = CPU_element([source], [result, source])
        b = CPU_element([result], [])
        with pytest.raises(TypeError):
            b.connect(a)
        with pytest.raises(TypeError):
            b.connect([5])
        b.connect([a])
        assert b.input_sources[result] == a
        assert source not in b.input_sources
        with pytest.raises(KeyError):
            b.connect([CPU_element([], [result])])

    def test_connect_multiple(self):
        names = "abcdfg"
        elements = [CPU_element([], [c]) for c in names]
        a = CPU_element(list(names), [])
        a.connect(elements)
        sources = {key:item for key, item in zip(names, elements)}
        assert sources == a.input_sources

    def test_read_input(self):
        a = CPU_element([source], [result])
        b = CPU_element([result], [])
        i = 42
        b.connect([a])
        a.outputs[result] = i
        assert b.inputs[result] == 0
        b.read_inputs()
        assert b.inputs[result] == i
        with pytest.raises(KeyError):
            a.read_inputs()
        with pytest.raises(TypeError):
            a.outputs[result] = "hei"
            b.read_inputs()

    def test_write_outputs(self):
        with pytest.raises(NotImplementedError):
            CPU_element([], []).write_outputs()
