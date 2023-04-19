# Copyright 2023 The Regents of the University of California
# released under BSD 3-Clause License
# author: Kevin Laeufer <laeufer@berkeley.edu>

from verilog_coverage import __version__


def test_version():
    assert __version__ == '0.1.0'
