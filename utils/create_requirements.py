import os
import ast

# pip install -r requirements.txt

# Manual includes - development and build tools that may not be detected
MANUAL_INCLUDES = {}

# Map module names to their corresponding PyPI package names
MODULE_TO_PACKAGE_MAP = {
    # Example: 'bson': 'pymongo',  # Not needed if bson is ignored
    'win32com': 'pywin32'
}

# Built-in modules to ignore (standard library)
IGNORED_BUILTINS = {
    'argparse', 'ast', 'asyncio', 'json', 'logging', 
    'os', 'sys', 'typing', 're', 'math', 'datetime', 
    'collections', 'functools', 'itertools', 'pkgutil',
    'time', 'subprocess', 'mmap', 'contextlib', 'enum',
    'traceback', 'urllib', 'inspect', 'secrets', 'ssl',
    'uuid', 'turtle', 'shutil', 'ctypes', 'dataclasses',
    'getpass', 'hashlib', 'http', 'platform', 'random',
    'socket', 'string', 'tempfile', 'unittest', 'zipfile',
    'threading', 'pathlib', 'email', 'smtplib', 'gc',
    'textwrap', 'csv'
}

# Directories with __init__.py (Python packages) to ignore
IGNORED_PACKAGE_DIRS = {
    # mine
    'cogs', 'components', 'core', 'events', 'handlers', 'models', 'routes', 'tasks', 'ui', 'utils',
    # third party
    'bson'
    # 'bson' is included with pymongo, so ignore it
}

# Directories without __init__.py (plain script folders) to ignore
IGNORED_SCRIPT_DIRS = {
    'archived', 'tests'
}

# Combine all things to ignore as modules
IGNORED_MODULES = set(IGNORED_BUILTINS) | set(IGNORED_PACKAGE_DIRS)

def filter_third_party_imports(imports):
    return [imp for imp in imports if imp not in IGNORED_MODULES]

def extract_all_imports(root_dir):
    imports = set()
    
    for dirpath, _, filenames in os.walk(root_dir):
        # Skip directories in the ignore list
        skip_dir = False
        for ignore_dir in IGNORED_SCRIPT_DIRS:
            if ignore_dir in dirpath.split(os.sep):
                skip_dir = True
                break
        if skip_dir:
            continue
            
        for filename in filenames:
            if filename.endswith('.py'):
                filepath = os.path.join(dirpath, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        try:
                            tree = ast.parse(file.read())
                            for node in ast.walk(tree):
                                # Direct imports
                                if isinstance(node, ast.Import):
                                    for n in node.names:
                                        imports.add(n.name.split('.')[0])
                                
                                # From imports
                                elif isinstance(node, ast.ImportFrom):
                                    if node.module:
                                        imports.add(node.module.split('.')[0])
                        except SyntaxError:
                            print(f"Syntax error in {filepath}")
                except UnicodeDecodeError:
                    print(f"Unicode decode error in {filepath} - skipping file")
    
    return sorted(imports)

def main(print_imports=False):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    all_imports = extract_all_imports(project_root)
    third_party_imports = filter_third_party_imports(all_imports)
    
    if print_imports:
        print("All detected imports:")
        print("Ignored built-in or local modules:")
        for imp in all_imports:
            if imp in IGNORED_MODULES:
                print(imp)
        
        print("\nThird-party imports:")
        for imp in third_party_imports:
            print(imp)
        
        print("\nMapped packages:")
        for imp in all_imports:
            if imp in MODULE_TO_PACKAGE_MAP:
                print(f"{imp} -> {MODULE_TO_PACKAGE_MAP[imp]}")
    
    # Write to requirements.txt
    requirements_path = os.path.join(project_root, 'requirements.txt')
    with open(requirements_path, 'w') as f:
        # Track packages already added to avoid duplicates
        added_packages = set()
        
        # First process mapped modules
        for imp in all_imports:
            if imp in MODULE_TO_PACKAGE_MAP and MODULE_TO_PACKAGE_MAP[imp] not in added_packages:
                package = MODULE_TO_PACKAGE_MAP[imp]
                f.write(f"{package}\n")
                added_packages.add(package)
        
        # Then process regular third-party imports
        for imp in third_party_imports:
            if imp not in MODULE_TO_PACKAGE_MAP and imp not in added_packages:
                f.write(f"{imp}\n")
                added_packages.add(imp)
        
        # Add manual includes
        for imp in MANUAL_INCLUDES:
            if imp not in added_packages:
                f.write(f"{imp}\n")
                added_packages.add(imp)
    
    print(f"\nRequirements written to {requirements_path}")

if __name__ == "__main__":
    main(print_imports=True)