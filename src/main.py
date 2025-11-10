# To test: cwd in src/, and then
#    uv run main.py test/task013.py
#    python main.py test/task013.py
# (not using any deps so far)

import sys
from minify import *

with open(sys.argv[1], 'r') as f:
    source_code = f.read()

print(minify(source_code))
