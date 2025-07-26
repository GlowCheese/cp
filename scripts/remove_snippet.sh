#!/usr/bin/env bash

read -p "• Name the snippet to remove: " name

.venv/bin/python -m utils.snippet_manager remove "$name"

exit_code=$?
if [[ $exit_code -eq 0 ]]; then
  echo "• Snippet '$name' removed"
fi

exit $exit_code
