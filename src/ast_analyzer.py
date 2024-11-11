# import ast
# from typing import Dict, Any

# class ASTAnalyzer(ast.NodeVisitor):
#     def __init__(self):
#         self.analysis = {
#             'functions': [],
#             'classes': [],
#             'imports': [],
#             'variables': [],
#             'loops': [],
#             'conditionals': []
#         }

#     def visit_FunctionDef(self, node):
#         self.analysis['functions'].append({
#             'name': node.name,
#             'args': [arg.arg for arg in node.args.args],
#             'lineno': node.lineno
#         })
#         self.generic_visit(node)

#     def visit_ClassDef(self, node):
#         self.analysis['classes'].append({
#             'name': node.name,
#             'lineno': node.lineno
#         })
#         self.generic_visit(node)

#     def visit_Import(self, node):
#         for alias in node.names:
#             self.analysis['imports'].append({
#                 'name': alias.name,
#                 'lineno': node.lineno
#             })

#     def visit_ImportFrom(self, node):
#         for alias in node.names:
#             self.analysis['imports'].append({
#                 'name': f"{node.module}.{alias.name}",
#                 'lineno': node.lineno
#             })

#     def visit_Assign(self, node):
#         for target in node.targets:
#             if isinstance(target, ast.Name):
#                 self.analysis['variables'].append({
#                     'name': target.id,
#                     'lineno': target.lineno
#                 })
#         self.generic_visit(node)

#     def visit_For(self, node):
#         self.analysis['loops'].append({
#             'type': 'for',
#             'lineno': node.lineno
#         })
#         self.generic_visit(node)

#     def visit_While(self, node):
#         self.analysis['loops'].append({
#             'type': 'while',
#             'lineno': node.lineno
#         })
#         self.generic_visit(node)

#     def visit_If(self, node):
#         self.analysis['conditionals'].append({
#             'type': 'if',
#             'lineno': node.lineno
#         })
#         self.generic_visit(node)

# def analyze_ast(tree: ast.AST) -> Dict[str, Any]:
#     analyzer = ASTAnalyzer()
#     analyzer.visit(tree)
#     return analyzer.analysis


# # def visit_If(self, node):
# #         self.analysis['conditionals'].append({
# #             'type': 'if',
# #             'lineno': node.lineno
# #         })
# #         self.generic_visit(node)
# #         for orelse_node in node.orelse:
# #             if isinstance(orelse_node, ast.If):
# #                 self.analysis['conditionals'].append({
# #                     'type': 'elif',
# #                     'lineno': orelse_node.lineno
# #                 })
# #                 self.visit(orelse_node)
# #             else:
# #                 self.visit(orelse_node)

import ast
from typing import Dict, Any, List

class ASTAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.analysis = []
        self.current_scope = self.analysis 

    def visit_FunctionDef(self, node):
        func_info = {
            'type': 'function',
            'name': node.name,
            'args': [arg.arg for arg in node.args.args],
            'body': [],
            'lineno': node.lineno
        }
        self.current_scope.append(func_info)
        previous_scope = self.current_scope
        self.current_scope = func_info['body']
        self.generic_visit(node)
        self.current_scope = previous_scope

    def visit_ClassDef(self, node):
        class_info = {
            'type': 'class',
            'name': node.name,
            'body': [],
            'lineno': node.lineno
        }
        self.current_scope.append(class_info)
        previous_scope = self.current_scope
        self.current_scope = class_info['body']
        self.generic_visit(node)
        self.current_scope = previous_scope

    def visit_Import(self, node):
        for alias in node.names:
            self.current_scope.append({
                'type': 'import',
                'name': alias.name,
                'lineno': node.lineno
            })

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.current_scope.append({
                'type': 'import',
                'name': f"{node.module}.{alias.name}",
                'lineno': node.lineno
            })

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.current_scope.append({
                    'type': 'variable',
                    'name': target.id,
                    'lineno': target.lineno
                })
        self.generic_visit(node)

    def visit_For(self, node):
        loop_info = {
            'type': 'for_loop',
            'body': [],
            'lineno': node.lineno
        }
        self.current_scope.append(loop_info)
        previous_scope = self.current_scope
        self.current_scope = loop_info['body']
        self.generic_visit(node)
        self.current_scope = previous_scope

    def visit_While(self, node):
        loop_info = {
            'type': 'while_loop',
            'body': [],
            'lineno': node.lineno
        }
        self.current_scope.append(loop_info)
        previous_scope = self.current_scope
        self.current_scope = loop_info['body']
        self.generic_visit(node)
        self.current_scope = previous_scope

    def visit_If(self, node):
        if_info = {
            'type': 'if_statement',
            'body': [],
            'lineno': node.lineno
        }
        self.current_scope.append(if_info)
        previous_scope = self.current_scope
        self.current_scope = if_info['body']
        self.generic_visit(node)
        self.current_scope = previous_scope

def analyze_ast(tree: ast.AST) -> List[Dict[str, Any]]:
    analyzer = ASTAnalyzer()
    analyzer.visit(tree)
    return analyzer.analysis