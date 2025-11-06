# To test: cwd in src/, and then
#    uv run main.py test/task013.py
#    python main.py test/task013.py
# (not using any deps so far)

import ast
import sys
from ast_transforms import *

with open(sys.argv[1], 'r') as f:
    source_code = f.read()

ast = ast.parse(source_code)

renamer = VariableRenamer()
transformed_tree = renamer.visit(ast)

ast.fix_missing_locations(transformed_tree)

new_code = ast.unparse(transformed_tree)

print(new_code)
