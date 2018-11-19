from cpu_element import CPU_element
from memory import Memory


def generate_test_file(d):
    lines = []
    file_name = "tests/test.mem"
    lines.append("# Docs")
    for address, value in d.items():
        lines.append("0x{:08x} 0x{:08x} #  Description".format(address, value))
    lines.append("# Final docs")
    with open(file_name, "w") as f:
        f.write("\n".join(lines))
    return file_name


class Test_Memory:
    def test_initialize_memory(self):
        lines = {i:i+i for i in range(10)}
        file_name = generate_test_file(lines)
        mem = Memory(file_name, [], [])
        assert isinstance(mem, CPU_element)
        assert mem.memory == lines

