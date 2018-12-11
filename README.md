Code written for Python 3.
Using pytest for testing.
if pytest is missing install it using:
* pip install pytest
Note on some systems with Python 2 and 3, pip may be known as pip3.

This code is supposed to lay a baseline for writing a simulator of
the datapath using the MIPS instruction set. It has been written such
that a writer in most cases should only need to implement the
write_outputs function. A new element should be subclassed from
CPU_element.

Control convention:
For elements that need control signals; it is recommended
to follow the convention of [control_names, input_names].
For example see Mux class in elements.py and tests/test_mux.py.

Duplicate output names:
Connect is set up such that a duplicate input names will raise
a Error. This can complicate setup for a pipeline approach; a suggestion
is to divide the stages into separate lists and connect in that way.

Click is a Python package for handling command line interface
that i can recommend. https://click.palletsprojects.com/en/7.x/

Recommended reading
* help(...); dict, list and zip in python.
* https://docs.python.org/3/library/index.html
