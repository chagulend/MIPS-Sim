import pytest
from cpu_element import CPU_element


class Test_CPU_element:
    def test_init(self):
        left = "Left"
        right = "Right"
        with pytest.raises(TypeError):
            CPU_element()
            CPU_element(left)
            CPU_element(left, right)
            CPU_element([1], [2])
        cpu = CPU_element([left], [right])
        assert left in cpu.inputs
        assert left not in cpu.outputs
        assert right in cpu.outputs
        assert right not in cpu.inputs

    def test_connect(self):
        left = "left"
        right = "right"
        a = CPU_element([left], [right])
        b = CPU_element([right], [left])
        with pytest.raises(TypeError):
            b.connect(a)
            b.connect(5)
            b.connect([5])
        b.connect([a])
        assert b.input_sources[right] == a
        with pytest.raises(KeyError):
            b.input_sources[left]
            b.connect([CPU_element([], [right])])

    def test_read_input(self):
        pass

    def test_write_output(self):
        with pytest.raises(NotImplementedError):
            CPU_element([], []).write_output()
