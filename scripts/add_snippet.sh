#!/usr/bin/env bash

read -p "• Snippet name: " name
read -p "• Snippet description: " description

temp_file="temp.cpp"
touch "$temp_file"

hx "$temp_file"

if [[ ! -s "$temp_file" ]]; then
  echo "! '$temp_file' is empty"
  rm -f "$temp_file"
  exit 1
fi

echo "---------- Snippet content ----------"
cat "$temp_file"
echo "-------------------------------------"

read -p "• Do you want to add the above snippet? (Y/n) " confirm

exit_code=0
if [[ "$confirm" == "Y" || "$confirm" == "y" || "$confirm" == "" ]]; then
  .venv/bin/python -m utils.snippet_manager add "$name" --src "$temp_file" --desc "$description"
  exit_code=$?

  if [[ $exit_code -eq 0 ]]; then
    echo "• Snippet '$name' added"
  fi
else
  echo "• Snippet not added"
fi

rm -f "$temp_file"
exit $exit_code
