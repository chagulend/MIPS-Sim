import pytest
from cpu_element import CPU_element
from memory import Memory
from tests.tools import set_signals


file_name = "tests/test.mem"


def file_ready(string):
    try:
        with open(file_name) as f:
            f_hash = hash(f.read())
    except FileNotFoundError:
        return False
    return f_hash == hash(string)


def generate_test_file(d):
    """ d = a dictionary."""
    lines = []
    lines.append("# Docs")
    for address, value in d.items():
        lines.append("0x{:08x} 0x{:08x} #  Description".format(address, value))
    lines.append("# Final docs")
    output = "\n".join(lines)
    if file_ready(output):
        return file_name
    with open(file_name, "w") as f:
        f.write(output)
    return file_name


class Test_Memory:
    def test_initialize_memory(self):
        lines = {i:i+i for i in range(10)}
        file_name = generate_test_file(lines)
        mem = Memory([], [])
        assert isinstance(mem, CPU_element)
        mem.initialize_memory(file_name)
        assert mem.memory == lines

    def test_write_outputs(self):
        with pytest.raises(NotImplementedError):
            Memory([], []).write_outputs()
