from typing import List, Dict, Any

TEMPLATES = {
    'function': "This code defines a function named '{name}' that takes {arg_count} argument(s): {args}.",
    'class': "This code defines a class named '{name}'.",
    'import': "This code imports the module or object '{name}'.",
    'variable': "This code declares a variable named '{name}'.",
    'for_loop': "This code starts a for loop.",
    'while_loop': "This code starts a while loop.",
    'if_statement': "This code starts an if statement for conditional execution."
}

def generate_explanation(analysis: List[Dict[str, Any]], indent: int = 0) -> str:
    explanations = []
    indent_str = "  " * indent

    for item in analysis:
        if item['type'] == 'function':
            explanation = TEMPLATES['function'].format(
                name=item['name'],
                arg_count=len(item['args']),
                args=', '.join(item['args'])
            )
            explanations.append(f"{indent_str}{explanation}")
            if item['body']:
                explanations.append(f"{indent_str}Inside this function:")
                explanations.append(generate_explanation(item['body'], indent + 1))

        elif item['type'] == 'class':
            explanation = TEMPLATES['class'].format(name=item['name'])
            explanations.append(f"{indent_str}{explanation}")
            if item['body']:
                explanations.append(f"{indent_str}Inside this class:")
                explanations.append(generate_explanation(item['body'], indent + 1))

        elif item['type'] == 'import':
            explanation = TEMPLATES['import'].format(name=item['name'])
            explanations.append(f"{indent_str}{explanation}")

        elif item['type'] == 'variable':
            explanation = TEMPLATES['variable'].format(name=item['name'])
            explanations.append(f"{indent_str}{explanation}")

        elif item['type'] in ['for_loop', 'while_loop']:
            explanation = TEMPLATES[item['type']]
            explanations.append(f"{indent_str}{explanation}")
            if item['body']:
                explanations.append(f"{indent_str}Inside this loop:")
                explanations.append(generate_explanation(item['body'], indent + 1))

        elif item['type'] == 'if_statement':
            explanation = TEMPLATES['if_statement']
            explanations.append(f"{indent_str}{explanation}")
            if item['body']:
                explanations.append(f"{indent_str}Inside this if statement:")
                explanations.append(generate_explanation(item['body'], indent + 1))

    return '\n'.join(explanations)