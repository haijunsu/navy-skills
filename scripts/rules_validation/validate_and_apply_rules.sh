#!/bin/bash
# validate_and_apply_rules.sh - Verify and apply AI rules

echo "Checking project AI rules configuration..."
python3 "$(dirname "$0")/apply_rules.py"
