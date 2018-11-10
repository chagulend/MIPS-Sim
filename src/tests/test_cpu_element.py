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
