"""
This is the first prototype of Mutest, a mutation testing tool that helps evaluate the quality of test suites. The prototype focuses on the core mutation engine: parsing source code, applying a small set of mutation operators (such as arithmetic, conditional, and logical changes), and preparing the foundation for test execution.

The goal of this prototype is to validate the parsing and mutation generation process and ensure the tool can reliably create mutants before integrating test execution, scoring, and reporting in later stages.

"""
import ast
import astor

code = "x = 1 + 2"
tree = ast.parse(code)

print(ast.dump(tree, indent=4))  # Built-in
print(astor.to_source(tree))     # Requires astor
