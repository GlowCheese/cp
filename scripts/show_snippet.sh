#!/usr/bin/env bash

read -p "• Snippet name: " name

.venv/bin/python -m utils.snippet_manager show "$name"
