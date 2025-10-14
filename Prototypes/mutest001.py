"""
This is the first prototype of Mutest, a mutation testing tool that helps evaluate
the quality of test suites. The prototype focuses on the core mutation engine:
parsing source code, applying a small set of mutation operators (such as arithmetic,
conditional, and logical changes), and preparing the foundation for test execution.

The goal of this prototype is to validate the parsing and mutation generation process
and ensure the tool can reliably create mutants before integrating test execution,
scoring, and reporting in later stages.
"""
import ast
import astor
import copy
import subprocess
import tempfile
import os
import shutil


# ============================================================================
# MUTATION OPERATORS
# ============================================================================

class MutationOperator(ast.NodeTransformer):
    """Base class for mutation operators"""

    def __init__(self):
        self.mutations = []

    def get_mutations(self):
        """Return list of mutations applied"""
        return self.mutations


class ArithmeticOperatorMutator(MutationOperator):
    """Mutates arithmetic operators: +, -, *, /, //, %, **"""

    MUTATIONS = {
        ast.Add: [ast.Sub, ast.Mult, ast.Div],
        ast.Sub: [ast.Add, ast.Mult, ast.Div],
        ast.Mult: [ast.Add, ast.Sub, ast.Div],
        ast.Div: [ast.Add, ast.Sub, ast.Mult],
        ast.FloorDiv: [ast.Div, ast.Mult],
        ast.Mod: [ast.Mult, ast.Div],
        ast.Pow: [ast.Mult, ast.Div],
    }

    def visit_BinOp(self, node):
        """Visit binary operation nodes and mutate operators"""
        self.generic_visit(node)

        op_type = type(node.op)
        if op_type in self.MUTATIONS:
            for mutation_op in self.MUTATIONS[op_type]:
                self.mutations.append({
                    'type': 'ArithmeticOperator',
                    'original': op_type.__name__,
                    'mutated': mutation_op.__name__,
                    'line': node.lineno,
                    'col': node.col_offset
                })

        return node


class ComparisonOperatorMutator(MutationOperator):
    """Mutates comparison operators: <, >, <=, >=, ==, !="""

    MUTATIONS = {
        ast.Lt: [ast.LtE, ast.Gt, ast.GtE],
        ast.LtE: [ast.Lt, ast.Gt, ast.GtE],
        ast.Gt: [ast.GtE, ast.Lt, ast.LtE],
        ast.GtE: [ast.Gt, ast.Lt, ast.LtE],
        ast.Eq: [ast.NotEq],
        ast.NotEq: [ast.Eq],
    }

    def visit_Compare(self, node):
        """Visit comparison nodes and mutate operators"""
        self.generic_visit(node)

        for i, op in enumerate(node.ops):
            op_type = type(op)
            if op_type in self.MUTATIONS:
                for mutation_op in self.MUTATIONS[op_type]:
                    self.mutations.append({
                        'type': 'ComparisonOperator',
                        'original': op_type.__name__,
                        'mutated': mutation_op.__name__,
                        'line': node.lineno,
                        'col': node.col_offset
                    })

        return node


class LogicalOperatorMutator(MutationOperator):
    """Mutates logical operators: and, or"""

    def visit_BoolOp(self, node):
        """Visit boolean operation nodes and mutate operators"""
        self.generic_visit(node)

        op_type = type(node.op)
        mutation_op = ast.Or if isinstance(node.op, ast.And) else ast.And

        self.mutations.append({
            'type': 'LogicalOperator',
            'original': op_type.__name__,
            'mutated': mutation_op.__name__,
            'line': node.lineno,
            'col': node.col_offset
        })

        return node


# ============================================================================
# SINGLE MUTATION APPLICATORS
# ============================================================================

class SingleArithmeticMutator(ast.NodeTransformer):
    """Applies a single arithmetic mutation"""

    def __init__(self, mutation_info):
        self.mutation_info = mutation_info
        self.applied = False

        self.op_map = {
            'Add': ast.Add, 'Sub': ast.Sub, 'Mult': ast.Mult,
            'Div': ast.Div, 'FloorDiv': ast.FloorDiv, 'Mod': ast.Mod,
            'Pow': ast.Pow
        }

    def visit_BinOp(self, node):
        self.generic_visit(node)

        if (not self.applied and
            node.lineno == self.mutation_info['line'] and
            type(node.op).__name__ == self.mutation_info['original']):

            node.op = self.op_map[self.mutation_info['mutated']]()
            self.applied = True

        return node


class SingleComparisonMutator(ast.NodeTransformer):
    """Applies a single comparison mutation"""

    def __init__(self, mutation_info):
        self.mutation_info = mutation_info
        self.applied = False

        self.op_map = {
            'Lt': ast.Lt, 'LtE': ast.LtE, 'Gt': ast.Gt,
            'GtE': ast.GtE, 'Eq': ast.Eq, 'NotEq': ast.NotEq
        }

    def visit_Compare(self, node):
        self.generic_visit(node)

        if (not self.applied and
            node.lineno == self.mutation_info['line']):

            for i, op in enumerate(node.ops):
                if type(op).__name__ == self.mutation_info['original']:
                    node.ops[i] = self.op_map[self.mutation_info['mutated']]()
                    self.applied = True
                    break

        return node


class SingleLogicalMutator(ast.NodeTransformer):
    """Applies a single logical mutation"""

    def __init__(self, mutation_info):
        self.mutation_info = mutation_info
        self.applied = False

    def visit_BoolOp(self, node):
        self.generic_visit(node)

        if (not self.applied and
            node.lineno == self.mutation_info['line']):

            if self.mutation_info['mutated'] == 'And':
                node.op = ast.And()
            else:
                node.op = ast.Or()
            self.applied = True

        return node


# ============================================================================
# MUTANT GENERATOR
# ============================================================================

class MutantGenerator:
    """Generates mutants by applying mutation operators to source code"""

    def __init__(self):
        self.operators = [
            ArithmeticOperatorMutator(),
            ComparisonOperatorMutator(),
            LogicalOperatorMutator()
        ]

    def generate_mutants(self, source_code):
        """
        Generate all possible mutants from source code

        Args:
            source_code: Python source code as string

        Returns:
            List of mutants, each containing:
                - code: The mutated source code
                - info: Details about the mutation
        """
        tree = ast.parse(source_code)
        mutants = []

        # Apply each operator
        for operator in self.operators:
            # Reset mutations for this operator
            operator.mutations = []

            # Visit the tree to find mutation points
            operator.visit(copy.deepcopy(tree))

            # Generate a mutant for each mutation point
            for mutation_info in operator.mutations:
                mutated_tree = self._apply_mutation(tree, mutation_info, operator)
                try:
                    mutated_code = astor.to_source(mutated_tree)
                    mutants.append({
                        'code': mutated_code,
                        'info': mutation_info
                    })
                except Exception as e:
                    print(f"Warning: Could not generate mutant: {e}")

        return mutants

    def _apply_mutation(self, tree, mutation_info, operator):
        """Apply a specific mutation to the tree"""
        mutated_tree = copy.deepcopy(tree)

        # Create a new instance of the operator for single mutation
        if mutation_info['type'] == 'ArithmeticOperator':
            mutator = SingleArithmeticMutator(mutation_info)
        elif mutation_info['type'] == 'ComparisonOperator':
            mutator = SingleComparisonMutator(mutation_info)
        elif mutation_info['type'] == 'LogicalOperator':
            mutator = SingleLogicalMutator(mutation_info)
        else:
            return mutated_tree

        return mutator.visit(mutated_tree)


# ============================================================================
# TEST EXECUTOR
# ============================================================================

class MutationTestExecutor:
    """Executes tests against mutants to determine if they are killed or survived"""

    def __init__(self, source_file_path, test_command="pytest"):
        """
        Args:
            source_file_path: Path to the source file to mutate
            test_command: Command to run tests (default: pytest)
        """
        self.source_file_path = source_file_path
        self.test_command = test_command
        self.results = []

    def run_original_tests(self):
        """Run tests on original code to ensure they pass"""
        print("Running tests on original code...")
        result = subprocess.run(
            self.test_command,
            shell=True,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print("WARNING: Original tests are failing!")
            print(result.stdout)
            print(result.stderr)
            return False

        print("Original tests passed!\n")
        return True

    def execute_mutant(self, mutant, mutant_number):
        """
        Execute tests against a single mutant

        Returns:
            dict with status ('killed' or 'survived') and details
        """
        # Read original file
        with open(self.source_file_path, 'r') as f:
            original_code = f.read()

        # Create backup
        backup_path = self.source_file_path + '.backup'
        shutil.copy(self.source_file_path, backup_path)

        try:
            # Write mutated code to source file
            with open(self.source_file_path, 'w') as f:
                f.write(mutant['code'])

            # Run tests
            result = subprocess.run(
                self.test_command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )

            # Determine if mutant was killed
            if result.returncode != 0:
                status = 'killed'
            else:
                status = 'survived'

            return {
                'mutant_number': mutant_number,
                'status': status,
                'mutation_info': mutant['info'],
                'return_code': result.returncode
            }

        except subprocess.TimeoutExpired:
            return {
                'mutant_number': mutant_number,
                'status': 'timeout',
                'mutation_info': mutant['info']
            }

        finally:
            # Restore original file
            shutil.move(backup_path, self.source_file_path)

    def run_mutation_tests(self, mutants):
        """
        Run tests against all mutants

        Returns:
            dict with killed, survived, and score
        """
        if not self.run_original_tests():
            print("Cannot proceed - original tests must pass first!")
            return None

        print(f"Testing {len(mutants)} mutants...\n")

        killed = []
        survived = []
        timeout = []

        for i, mutant in enumerate(mutants, 1):
            print(f"Testing mutant {i}/{len(mutants)}: "
                  f"{mutant['info']['type']} at line {mutant['info']['line']} "
                  f"({mutant['info']['original']} -> {mutant['info']['mutated']})...",
                  end=" ")

            result = self.execute_mutant(mutant, i)

            if result['status'] == 'killed':
                print("KILLED")
                killed.append(result)
            elif result['status'] == 'survived':
                print("SURVIVED")
                survived.append(result)
            else:
                print("TIMEOUT")
                timeout.append(result)

        # Calculate mutation score
        total = len(mutants)
        killed_count = len(killed)
        survived_count = len(survived)
        timeout_count = len(timeout)

        if total > 0:
            mutation_score = (killed_count / total) * 100
        else:
            mutation_score = 0

        return {
            'total': total,
            'killed': killed,
            'survived': survived,
            'timeout': timeout,
            'killed_count': killed_count,
            'survived_count': survived_count,
            'timeout_count': timeout_count,
            'mutation_score': mutation_score
        }


# ============================================================================
# REPORTER
# ============================================================================

def print_mutation_report(results):
    """Print a detailed mutation testing report"""
    print("\n" + "=" * 60)
    print("MUTATION TESTING REPORT")
    print("=" * 60)

    print(f"\nTotal Mutants: {results['total']}")
    print(f"Killed: {results['killed_count']}")
    print(f"Survived: {results['survived_count']}")
    print(f"Timeout: {results['timeout_count']}")
    print(f"\nMutation Score: {results['mutation_score']:.2f}%")

    if results['survived']:
        print("\n" + "-" * 60)
        print("SURVIVED MUTANTS (Weak Test Coverage):")
        print("-" * 60)
        for mutant in results['survived']:
            info = mutant['mutation_info']
            print(f"\nMutant #{mutant['mutant_number']}:")
            print(f"  Type: {info['type']}")
            print(f"  Line {info['line']}: {info['original']} -> {info['mutated']}")

    print("\n" + "=" * 60)


# ============================================================================
# DEMO / TEST
# ============================================================================

if __name__ == "__main__":
    import sys

    print("=" * 60)
    print("MUTEST001 - Mutation Testing Prototype")
    print("=" * 60)

    # Example usage with math_utils.py
    source_file = "testing/simple_funcitons/math_utils.py"
    test_command = "python -m pytest testing/tests/test_001.py -v"

    if len(sys.argv) > 1:
        source_file = sys.argv[1]
    if len(sys.argv) > 2:
        test_command = sys.argv[2]

    print(f"\nSource file: {source_file}")
    print(f"Test command: {test_command}\n")

    # Read source code
    try:
        with open(source_file, 'r') as f:
            source_code = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find file '{source_file}'")
        print("\nUsage: python mutest001.py [source_file] [test_command]")
        print("Example: python mutest001.py testing/simple_funcitons/math_utils.py \"pytest testing/tests/\"")
        sys.exit(1)

    # Generate mutants
    print("Generating mutants...")
    generator = MutantGenerator()
    mutants = generator.generate_mutants(source_code)
    print(f"Generated {len(mutants)} mutants.\n")

    # Run mutation tests
    executor = MutationTestExecutor(source_file, test_command)
    results = executor.run_mutation_tests(mutants)

    if results:
        print_mutation_report(results)
