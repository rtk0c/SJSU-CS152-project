import ast
from itertools import count, product
import string


iden0 = string.ascii_letters + '_'
idenN1 = iden0 + string.digits

def shortnames_generator():
    # len 1 iden
    for c in iden0:
        yield c
    # len 2, 3, ... iden
    for length in count(start=2):
        for char0 in iden0:
            for charN1 in product(idenN1, repeat=length - 1):
                yield char0 + ''.join(charN1)


class VariableRenamer(ast.NodeTransformer):
    def __init__(self):
        self.name_generator = shortnames_generator()
        self.name_map = {}
        self.builtins = set(dir(__builtins__))
    
    def gen_shortname(self, old_name):
        if old_name not in self.name_map:
            if old_name not in self.builtins:
                new_name = next(self.name_generator)
                self.name_map[old_name] = new_name
            else:
                self.name_map[old_name] = old_name
        return self.name_map[old_name]
    
    def visit_Name(self, node):
        self.generic_visit(node)
        node.id = self.gen_shortname(node.id)
        return node
    
    def visit_arg(self, node):
        self.generic_visit(node)
        node.arg = self.gen_shortname(node.arg)
        return node
    
    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        node.name = self.gen_shortname(node.name)
        return node
    
    def visit_AsyncFunctionDef(self, node):
        self.generic_visit(node)
        node.name = self.gen_shortname(node.name)
        return node
    
    def visit_ClassDef(self, node):
        self.generic_visit(node)
        node.name = self.gen_shortname(node.name)
        return node
    
    def visit_Global(self, node):
        node.names = [self.gen_shortname(name) for name in node.names]
        return node
    
    def visit_Nonlocal(self, node):
        node.names = [self.gen_shortname(name) for name in node.names]
        return node
