import ast

def validate_python_code(code: str) -> bool:
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False

def preprocess_code(code: str) -> str:
    # Remove leading/trailing whitespace and normalize line endings
    return code.strip().replace('\r\n', '\n')

def parse_code(code: str) -> ast.AST:
    preprocessed_code = preprocess_code(code)
    if not validate_python_code(preprocessed_code):
        raise ValueError("Invalid Python code")
    return ast.parse(preprocessed_code)