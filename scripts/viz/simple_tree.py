# Usage: python ./scripts/viz/simple_tree.py
# Description: Generates a simple tree structure of the project directory

import os
from gitignore_parser import parse_gitignore

def is_ignored(file_path, matches):
    return matches(file_path)

def list_directory_structure(path, matches, output_file, indent='', is_root=False):
    entries = sorted(os.listdir(path))
    
    dirs = [entry for entry in entries if os.path.isdir(os.path.join(path, entry)) and not is_ignored(os.path.join(path, entry), matches)]
    files = [entry for entry in entries if os.path.isfile(os.path.join(path, entry)) and not is_ignored(os.path.join(path, entry), matches)]

    vue_files = [file for file in files if file.endswith('.vue')]
    
    if len(vue_files) > 10:
        extra_count = len(vue_files) - 5
        vue_files = vue_files[:5] + [f"(+ {extra_count} .vue files)"]

    if is_root:
        for file in files:
            output_file.write(f"{file}\n")
    else:
        for file in vue_files:
            output_file.write(f"{indent}{file}\n")
        
        for file in files:
            if not file.endswith('.vue'):
                output_file.write(f"{indent}{file}\n")

    for directory in dirs:
        dir_path = os.path.join(path, directory)
        output_file.write(f"{indent}{directory}/\n")
        list_directory_structure(dir_path, matches, output_file, indent + '\t')

def generate_tree_structure(root_dir, gitignore_file, output_path):
    matches = parse_gitignore(gitignore_file)

    with open(output_path, 'w') as output_file:
        list_directory_structure(root_dir, matches, output_file, is_root=True)

root_dir = '.'
gitignore_file = os.path.join(root_dir, '.gitignore')
output_path = './assets/simple_tree.txt'

generate_tree_structure(root_dir, gitignore_file, output_path)
