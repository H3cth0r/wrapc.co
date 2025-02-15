import re

def extract_function_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    function_pattern = re.compile(r'^[\s]*(?:inline\s+)?[a-zA-Z_][a-zA-Z0-9_:<>]*\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\([^)]*\)\s*\{')
    
    function_names = []
    
    for line in content:
        match = function_pattern.match(line)
        if match:
            function_names.append(match.group(1))
    
    return function_names

# Example usage
file_path = "my_library.hpp"
functions = extract_function_names(file_path)
print(functions)
