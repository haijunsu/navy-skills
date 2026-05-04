import os
import sys

def verify_and_apply():
    project_root = os.getcwd()
    ai_rules_dir = os.path.join(project_root, 'ai-rules')

    if not os.path.isdir(ai_rules_dir):
        print(f"Error: 'ai-rules' directory not found at {ai_rules_dir}")
        print("Please add it as a submodule first: git submodule add git@github.com:haijunsu/navy-skills.git ai-rules")
        sys.exit(1)

    configs = {
        'CLAUDE.md': {
            'content': "# CLAUDE.md\nRules for this repository are managed in the `ai-rules/` submodule.\n",
            'check': 'ai-rules/'
        },
        'GEMINI.md': {
            'content': "# Project Instructions\nThis project adheres to the standards defined in the `ai-rules/` submodule.\n\n## Rule Index\n- [Tech Stack](ai-rules/stack.md)\n- [Code Style](ai-rules/code-style.md)\n- [Workflow](ai-rules/workflow.md)\n",
            'check': 'ai-rules/stack.md'
        },
        '.github/copilot-instructions.md': {
            'content': "# Copilot Instructions\nFollow the project standards and workflows defined in the `ai-rules/` directory:\n- Tech Stack: ai-rules/stack.md\n- Code Style: ai-rules/code-style.md\n- Workflow: ai-rules/workflow.md\n",
            'check': 'ai-rules/stack.md'
        },
        'AGENTS.md': {
            'content': "# AGENTS.md\nRules for this repository are managed in the `ai-rules/` submodule.\nRefer to the rules in:\n- [ai-rules/stack.md](ai-rules/stack.md)\n- [ai-rules/code-style.md](ai-rules/code-style.md)\n- [ai-rules/workflow.md](ai-rules/workflow.md)\n",
            'check': 'ai-rules/stack.md'
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
