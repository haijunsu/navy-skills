import os
import sys
import subprocess

def get_git_root():
    try:
        # Try to get the superproject root first (if we are in a submodule)
        superproject = subprocess.check_output(
            ['git', 'rev-parse', '--show-superproject-working-tree'],
            stderr=subprocess.STDOUT
        ).decode('utf-8').strip()
        
        if superproject:
            return superproject
            
        # Fallback to the current repository root
        return subprocess.check_output(
            ['git', 'rev-parse', '--show-toplevel'],
            stderr=subprocess.STDOUT
        ).decode('utf-8').strip()
    except subprocess.CalledProcessError:
        # Fallback to directory-based detection if git fails
        script_path = os.path.abspath(__file__)
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(script_path))))

def verify_and_apply():
    # Identify where the rules submodule is located relative to the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    submodule_root = os.path.dirname(os.path.dirname(script_dir))
    submodule_name = os.path.basename(submodule_root)
    
    project_root = get_git_root()

    print(f"Detected project root: {project_root}")
    print(f"Detected submodule name: {submodule_name}")

    if not os.path.isdir(submodule_root):
        print(f"Error: Submodule directory not found at {submodule_root}")
        sys.exit(1)

    configs = {
        'CLAUDE.md': {
            'content': f"# CLAUDE.md\nRules for this repository are managed in the `{submodule_name}/ai-rules/` directory.\n",
            'check': f'{submodule_name}/ai-rules/'
        },
        'GEMINI.md': {
            'content': f"# Project Instructions\nThis project adheres to the standards defined in the `{submodule_name}/ai-rules/` directory.\n\n## Rule Index\n- [Tech Stack]({submodule_name}/ai-rules/stack.md)\n- [Code Style]({submodule_name}/ai-rules/code-style.md)\n- [Workflow]({submodule_name}/ai-rules/workflow.md)\n",
            'check': f'{submodule_name}/ai-rules/stack.md'
        },
        '.github/copilot-instructions.md': {
            'content': f"# Copilot Instructions\nFollow the project standards and workflows defined in the `{submodule_name}/ai-rules/` directory:\n- Tech Stack: {submodule_name}/ai-rules/stack.md\n- Code Style: {submodule_name}/ai-rules/code-style.md\n- Workflow: {submodule_name}/ai-rules/workflow.md\n",
            'check': f'{submodule_name}/ai-rules/stack.md'
        },
        'AGENTS.md': {
            'content': f"# AGENTS.md\nRules for this repository are managed in the `{submodule_name}/ai-rules/` directory.\nRefer to the rules in:\n- [{submodule_name}/ai-rules/stack.md]({submodule_name}/ai-rules/stack.md)\n- [{submodule_name}/ai-rules/code-style.md]({submodule_name}/ai-rules/code-style.md)\n- [{submodule_name}/ai-rules/workflow.md]({submodule_name}/ai-rules/workflow.md)\n",
            'check': f'{submodule_name}/ai-rules/stack.md'
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
