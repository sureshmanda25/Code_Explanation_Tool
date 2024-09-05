import ast
from typing import Dict, Any

class ASTAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.analysis = {
            'functions': [],
            'classes': [],
            'imports': [],
            'variables': [],
            'loops': [],
            'conditionals': []
        }

    def visit_FunctionDef(self, node):
        self.analysis['functions'].append({
            'name': node.name,
            'args': [arg.arg for arg in node.args.args],
            'lineno': node.lineno
        })
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.analysis['classes'].append({
            'name': node.name,
            'lineno': node.lineno
        })
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            self.analysis['imports'].append({
                'name': alias.name,
                'lineno': node.lineno
            })

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.analysis['imports'].append({
                'name': f"{node.module}.{alias.name}",
                'lineno': node.lineno
            })

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.analysis['variables'].append({
                    'name': target.id,
                    'lineno': target.lineno
                })
        self.generic_visit(node)

    def visit_For(self, node):
        self.analysis['loops'].append({
            'type': 'for',
            'lineno': node.lineno
        })
        self.generic_visit(node)

    def visit_While(self, node):
        self.analysis['loops'].append({
            'type': 'while',
            'lineno': node.lineno
        })
        self.generic_visit(node)

    def visit_If(self, node):
        self.analysis['conditionals'].append({
            'type': 'if',
            'lineno': node.lineno
        })
        self.generic_visit(node)

def analyze_ast(tree: ast.AST) -> Dict[str, Any]:
    analyzer = ASTAnalyzer()
    analyzer.visit(tree)
    return analyzer.analysis


# def visit_If(self, node):
#         self.analysis['conditionals'].append({
#             'type': 'if',
#             'lineno': node.lineno
#         })
#         self.generic_visit(node)
#         for orelse_node in node.orelse:
#             if isinstance(orelse_node, ast.If):
#                 self.analysis['conditionals'].append({
#                     'type': 'elif',
#                     'lineno': orelse_node.lineno
#                 })
#                 self.visit(orelse_node)
#             else:
#                 self.visit(orelse_node)