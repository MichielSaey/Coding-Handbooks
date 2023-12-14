import ast
import re
import os
import sys
from _ast import FunctionDef, Assign, AST, ClassDef

# error codes
error_codes = {
    1: 'S001 Too long',
    2: 'S002 Indentation is not a multiple of four',
    3: 'S003 Unnecessary semicolon',
    4: 'S004 At least two spaces required before inline comments',
    5: 'S005 TODO found',
    6: 'S006 More than two blank lines used before this line',
    7: 'Too many spaces after construction_name (def or class)',
    8: 'Class name class_name should be written in CamelCase',
    9: 'Function name function_name should be written in snake_case'
}


def scantree(path):
    entry: os.DirEntry
    for entry in os.scandir(path):
        # for entry in os.scandir(os.path.join(parent, path)):
        if entry.is_dir(follow_symlinks=False):
            if entry.path:
                yield from scantree(entry.path)
        else:
            yield entry


def print_error(file_path, line, error):
    print(f'{file_path}: Line {line}: {error_codes[error]}')

class Analyzer(ast.NodeVisitor):
    def __init__(self, file_path):
        self.file_path = file_path
        self.errors = []

    def print_error(self ,line, error):
        print(f'{self.file_path}: Line {line}: {error_codes[error]}')

    # def visit(self, node: AST):
    #    print(node)

    # S008: camel case class name
    def visit_ClassDef(self, node: ClassDef):

        # S008
        camel_case = re.match("[A-Z][a-zA-Z]+", node.name)
        if not camel_case:
            self.errors.append(f"{self.file_path}: Line {node.lineno}: S008 Class name '{node.name}' should use CamelCase")
        self.generic_visit(node)

    # S009: function name snake_case
    # S010: argument name snake_case
    # S012: default argument mutable
    def visit_FunctionDef(self, node: FunctionDef):

        # S009
        snake_case = re.match("^[a-z_]", node.name)
        if not snake_case:
            self.errors.append(f"{self.file_path}: Line {node.lineno}: S009 Function name '{node.name}' should use snake_case")

        # S010
        for arg in node.args.args:
            argument = arg.arg
            snake_case = re.match("^[a-z_]", argument)
            if not snake_case:
                self.errors.append(f"{self.file_path}: Line {node.lineno}: S010 Argument name '{argument}' should be snake_case")
                break

        # S012
        for arg in node.args.defaults:
            if isinstance(arg, ast.List) or isinstance(arg, ast.Dict):
                self.errors.append(f"{self.file_path}: Line {node.lineno}: S012 Default argument value is mutable")
                break

        self.generic_visit(node)

    # S011: variable name snake_case
    def visit_Assign(self, node: Assign):
        for target in node.targets:
            if hasattr(target, 'id'):
                name = target.id
            else:
                name = target.attr
            snake_case = re.match("^[a-z_]", name)
            if not snake_case:
                self.errors.append(f"{self.file_path}: Line {node.lineno}: S011 Variable '{name}' in function should be snake_case")
                break
        self.generic_visit(node)



def read_file(file_path):
    # print(file_path)
    errors = []
    try:
        if "tests.py" in file_path:
            pass
        else:
            with open(file_path, 'r', encoding='utf8') as file:
                # for S006
                n_white_lines = 0
                for n, line in enumerate(file.readlines()):
                    # for S006
                    if line == "\n":
                        n_white_lines += 1
                        continue
                    # could be rewriten into severate function, but for now im to lazy
                    # calculate properties of line
                    # S001
                    length = len(line)
                    # S002
                    indentation_count = length - len(line.lstrip(' '))
                    # S003
                    no_semicolon = re.search('^([^#])*;(?!\S)', line)
                    # S004
                    no_two_spaces = re.match(r"[^#]*[^ ]( ?#)", line)
                    # S005
                    no_todo = re.match('(?i).*# TODO.*', line)

                    # check them
                    try:
                        assert length < 80, f'{file_path}: Line {n + 1}: {error_codes[1]}'
                    except AssertionError as err:
                        errors.append(err)

                    try:
                        assert indentation_count % 4 == 0, f'{file_path}: Line {n + 1}: {error_codes[2]}'
                    except AssertionError as err:
                        errors.append(err)
                    try:
                        assert not no_semicolon, f'{file_path}: Line {n + 1}: {error_codes[3]}'
                    except AssertionError as err:
                        errors.append(err)
                    try:
                        assert not no_two_spaces, f'{file_path}: Line {n + 1}: {error_codes[4]}'
                    except AssertionError as err:
                        errors.append(err)
                    try:
                        assert not no_todo, f'{file_path}: Line {n + 1}: {error_codes[5]}'
                    except AssertionError as err:
                        errors.append(err)
                    try:
                        assert n_white_lines < 3, f'{file_path}: Line {n + 1}: {error_codes[6]}'
                    except AssertionError as err:
                        errors.append(err)

                    # S006 reset white lines after catch
                    if line != "\n":
                        n_white_lines = 0

                    # S007
                    # count spaces after class or def
                    # this can be done using a regex and find all
                    start_with_class = re.match(r"^class", line)
                    start_with_def = re.search("def", line)
                    word_size = 0
                    index = 0

                    if start_with_class:
                        word_size = 5
                    elif start_with_def:
                        word_size = start_with_def.span()[1]

                    space_count = 0
                    if word_size != 0:
                        for i in range(word_size, len(line)):
                            index = i
                            if line[i] == " ":
                                space_count += 1
                            else:
                                break
                        if space_count > 1:
                            name = line.lstrip().split(" ")[0]
                            errors.append(f"{file_path}: Line {n + 1}: S007 Too many spaces after '{name}'")

    except Exception as e:
        pass

    return errors


if __name__ == "__main__":
    argument = sys.argv

    # argument = ['code_analyzer.py', 'test\\this_stage\\test_7.py'] # to perform testing with run
    # argument = ['code_analyzer.py', r'C:\Users\michi\PycharmProjects\Static Code Analyzer\Static Code Analyzer\task\test\test_1.py'] # to perform testing with run
    # argument = ['code_analyzer.py', r"C:\Users\michi\PycharmProjects\Static Code Analyzer\Static Code Analyzer\task\test\this_stage\test_3.py"]

    # print(argument)

    path = argument[1]
    errors = []

    if path.endswith(".py"):
        errors = errors + read_file(path)
        analyzer = Analyzer(path)
        with open(path) as file:
            tree = ast.parse(file.read())
            analyzer.visit(tree)
            errors = errors + analyzer.errors
    else:
        entry: os.DirEntry
        for entry in scantree(path):
            if entry.path:
                errors = errors + read_file(entry.path)
                analyzer = Analyzer(entry.path)
                with open(entry.path) as file:
                    tree = ast.parse(file.read())
                    analyzer.visit(tree)
                    errors = errors + analyzer.errors

    for i in errors:
        print(i)
