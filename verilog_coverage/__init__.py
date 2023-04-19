# Copyright 2023 The Regents of the University of California
# released under BSD 3-Clause License
# author: Kevin Laeufer <laeufer@berkeley.edu>

from pyslang import *

__version__ = '0.1.0'


test = """
module test(input clk, input a, input b, output c);
  always 
endmodule
"""


def main():
    print("Test")

    tree = SyntaxTree.fromText(test)
    print(tree)
    comp = Compilation()
    comp.addSyntaxTree(tree)
    diags = comp.getAllDiagnostics()
    report = DiagnosticEngine.reportAll(comp.sourceManager, diags)
    print(report)



if __name__ == '__main__':
    main()