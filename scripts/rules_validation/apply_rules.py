import os
import sys
import subprocess

def get_git_root():
    try:
        # Try to get the superproject root first (if we are in a submodule)
        # git rev-parse --show-superproject-working-tree returns the root of the superproject
        superproject = subprocess.check_output(
            ['git', 'rev-parse', '--show-superproject-working-tree'],
            stderr=subprocess.STDOUT
        ).decode('utf-8').strip()
        
        if superproject:
            return os.path.abspath(superproject)
            
        # Fallback to the current repository root
        return os.path.abspath(subprocess.check_output(
            ['git', 'rev-parse', '--show-toplevel'],
            stderr=subprocess.STDOUT
        ).decode('utf-8').strip())
    except subprocess.CalledProcessError:
        # Fallback to directory-based detection if git fails
        # script is at <root>/scripts/rules_validation/apply_rules.py
        script_path = os.path.abspath(__file__)
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(script_path))))

def verify_and_apply():
    # 1. Get the project root (where the .git folder or superproject root is)
    project_root = get_git_root()
    
    # 2. Get the absolute path to the rules folder
    # This script is at <submodule>/scripts/rules_validation/apply_rules.py
    # The rules are at <submodule>/ai-rules/
    script_dir = os.path.dirname(os.path.abspath(__file__))
    rules_dir_abs = os.path.abspath(os.path.join(script_dir, '..', '..', 'ai-rules'))

    # 3. Calculate the relative path from project root to rules
    rules_rel_path = os.path.relpath(rules_dir_abs, project_root)

    print(f"--- AI Rules Configuration ---")
    print(f"Project Root: {project_root}")
    print(f"Rules Path (Abs): {rules_dir_abs}")
    print(f"Rules Path (Rel): {rules_rel_path}")
    print(f"-------------------------------")

    if not os.path.isdir(rules_dir_abs):
        print(f"Error: Rules directory not found at {rules_dir_abs}")
        sys.exit(1)

    configs = {
        'CLAUDE.md': {
            'content': f"# CLAUDE.md\nRules for this repository are managed in the `{rules_rel_path}/` directory.\n",
            'check': f'{rules_rel_path}/'
        },
        'GEMINI.md': {
            'content': f"# Project Instructions\nThis project adheres to the standards defined in the `{rules_rel_path}/` directory.\n\n## Rule Index\n- [Tech Stack]({rules_rel_path}/stack.md)\n- [Code Style]({rules_rel_path}/code-style.md)\n- [Workflow]({rules_rel_path}/workflow.md)\n",
            'check': f'{rules_rel_path}/stack.md'
        },
        '.github/copilot-instructions.md': {
            'content': f"# Copilot Instructions\nFollow the project standards and workflows defined in the `{rules_rel_path}/` directory:\n- Tech Stack: {rules_rel_path}/stack.md\n- Code Style: {rules_rel_path}/code-style.md\n- Workflow: {rules_rel_path}/workflow.md\n",
            'check': f'{rules_rel_path}/stack.md'
        },
        'AGENTS.md': {
            'content': f"# AGENTS.md\nRules for this repository are managed in the `{rules_rel_path}/` directory.\nRefer to the rules in:\n- [{rules_rel_path}/stack.md]({rules_rel_path}/stack.md)\n- [{rules_rel_path}/code-style.md]({rules_rel_path}/code-style.md)\n- [{rules_rel_path}/workflow.md]({rules_rel_path}/workflow.md)\n",
            'check': f'{rules_rel_path}/stack.md'
        }
    }

    for file_path, data in configs.items():
        full_path = os.path.join(project_root, file_path)
        dir_name = os.path.dirname(full_path)
        
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)

        is_valid = False
        if os.path.exists(full_path):
            with open(full_path, 'r') as f:
                content = f.read()
                if data['check'] in content:
                    is_valid = True
        
        if not is_valid:
            print(f"Applying/Updating {file_path}...")
            with open(full_path, 'w') as f:
                f.write(data['content'])
        else:
            print(f"Verified {file_path}: OK")

if __name__ == "__main__":
    verify_and_apply()
