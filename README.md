Code written for Python 3.
Using pytest for testing.
if pytest is missing install it using:
* pip install pytest

Note on some systems with Python 2 and 3, pip may be known as pip3.

This code is intended for educational purposes. It is designed as a
starting point for simulating a datapath. The fundament is based
of the MIPS architecture.
It has been written such
that a writer in most cases should only need to implement the
write_outputs function. A new element should be subclassed from
CPU_element.
