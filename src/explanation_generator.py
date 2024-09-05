from typing import Dict, Any

TEMPLATES = {
    'function': "This code defines a function named '{name}' that takes {arg_count} argument(s): {args}.",
    'class': "This code defines a class named '{name}'.",
    'import': "This code imports the module or object '{name}'.",
    'variable': "This code declares a variable named '{name}'.",
    'for_loop': "This code starts a for loop.",
    'while_loop': "This code starts a while loop.",
    'if_statement': "This code starts an if statement for conditional execution."
}

def generate_explanation(analysis: Dict[str, Any]) -> str:
    explanations = []

    for func in analysis['functions']:
        explanations.append(TEMPLATES['function'].format(
            name=func['name'],
            arg_count=len(func['args']),
            args=', '.join(func['args'])
        ))

    for cls in analysis['classes']:
        explanations.append(TEMPLATES['class'].format(name=cls['name']))

    for imp in analysis['imports']:
        explanations.append(TEMPLATES['import'].format(name=imp['name']))

    for var in analysis['variables']:
        explanations.append(TEMPLATES['variable'].format(name=var['name']))

    for loop in analysis['loops']:
        if loop['type'] == 'for':
            explanations.append(TEMPLATES['for_loop'])
        elif loop['type'] == 'while':
            explanations.append(TEMPLATES['while_loop'])

    for cond in analysis['conditionals']:
        explanations.append(TEMPLATES['if_statement'])

    return '\n'.join(explanations)