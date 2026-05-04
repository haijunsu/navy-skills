import os
import sys
import subprocess

def get_git_root():
    try:
        # Try to find the superproject root (if we are in a submodule)
        superproject = subprocess.check_output(
            ['git', 'rev-parse', '--show-superproject-working-tree'],
            stderr=subprocess.STDOUT
        ).decode('utf-8').strip()
        
        if superproject:
            return os.path.abspath(superproject)
            
        # If not in a submodule, get the current repo root
        return os.path.abspath(subprocess.check_output(
            ['git', 'rev-parse', '--show-toplevel'],
            stderr=subprocess.STDOUT
        ).decode('utf-8').strip())
    except subprocess.CalledProcessError:
        script_path = os.path.abspath(__file__)
        return os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(script_path))))

def verify_and_apply():
    project_root = get_git_root()
    
    # Locate the rules directory relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    rules_dir_abs = os.path.abspath(os.path.join(script_dir, '..', '..', 'ai-rules'))

    if not os.path.isdir(rules_dir_abs):
        print(f"Error: Rules directory not found at {rules_dir_abs}")
        sys.exit(1)

    # Calculate relative path to rules for the agent files
    rules_rel_path = os.path.relpath(rules_dir_abs, project_root)
    
    # Discovery: Find all rule files
    rule_files = sorted([f for f in os.listdir(rules_dir_abs) if f.endswith('.md')])
    
    print(f"--- AI Rules Configuration ---")
    print(f"Project Root: {project_root}")
    print(f"Rules Path (Rel): {rules_rel_path}")
    print(f"Discovered Rules: {', '.join(rule_files)}")
    print(f"-------------------------------")

    # Mapping rule filenames to descriptive labels for display
    def get_label(filename):
        name = filename.replace('.md', '').replace('-', ' ').replace('_', ' ')
        return name.title()

    # Define configurations
    configs = {
        'CLAUDE.md': {
            'header': "# CLAUDE.md\nRules for this repository are managed in the centralized rules directory.\n\n## Project Rules\n",
            'item_fmt': "- **{label}**: [{path}]({path})\n",
            'path': 'CLAUDE.md'
        },
        'GEMINI.md': {
            'header': "# Project Instructions\nThis project adheres to the standards defined in the centralized rules directory.\n\n## Rule Index\n",
            'item_fmt': "- [{label}]({path})\n",
            'path': 'GEMINI.md'
        },
        '.github/copilot-instructions.md': {
            'header': "# Copilot Instructions\nFollow the project standards and workflows defined in the rules directory:\n",
            'item_fmt': "- {label}: {path}\n",
            'path': '.github/copilot-instructions.md'
        },
        'AGENTS.md': {
            'header': "# AGENTS.md\nRules for this repository are managed in the centralized rules directory.\nRefer to the rules in:\n",
            'item_fmt': "- [{path}]({path})\n",
            'path': 'AGENTS.md'
        }
    }

    for name, cfg in configs.items():
        full_path = os.path.join(project_root, cfg['path'])
        dir_name = os.path.dirname(full_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)

        # Build expected content
        new_content = cfg['header']
        for rf in rule_files:
            rel_rf = os.path.join(rules_rel_path, rf)
            new_content += cfg['item_fmt'].format(label=get_label(rf), path=rel_rf)

        # Verification
        needs_update = True
        if os.path.exists(full_path):
            with open(full_path, 'r') as f:
                current_content = f.read()
                # Check if all rules are present
                if all(os.path.join(rules_rel_path, rf) in current_content for rf in rule_files):
                    # Also check header to ensure pathing is correct (no old prefixes)
                    if cfg['header'] in current_content or f"managed in the `{rules_rel_path}/`" in current_content:
                         needs_update = False

        if needs_update:
            print(f"Updating {cfg['path']}...")
            with open(full_path, 'w') as f:
                f.write(new_content)
        else:
            print(f"Verified {cfg['path']}: OK (All rules present)")

if __name__ == "__main__":
    verify_and_apply()
