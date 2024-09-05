from input_handler import parse_code
from ast_analyzer import analyze_ast
from explanation_generator import generate_explanation
from nlp_processor import process_text

def explain_code(code: str) -> str:
    try:
        ast_tree = parse_code(code)
        analysis = analyze_ast(ast_tree)
        raw_explanation = generate_explanation(analysis)
        processed_explanation = process_text(raw_explanation)
        return processed_explanation
    except ValueError as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Example usage
    sample_code = """
def greet(name):
    print(f"Hello, {name}!")

class Person:
    def __init__(self, name):
        self.name = name

import math

x = 10
y = int(input("y = "))
if x > 5:
    for i in range(x):
        print(i)
    """
    
    explanation = explain_code(sample_code)
    print(explanation)