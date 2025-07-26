import argparse
import json
from pathlib import Path
from typing import Optional

json_path = Path(".helix/snippets/cpp.json")

if not json_path.exists():
    data = {}
else:
    with json_path.open("r", encoding="utf-8") as file:
        data = json.load(file)


def _write_data():
    with json_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def _load_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    parser_a = subparsers.add_parser("add")
    parser_a.add_argument("name", type=str, help="Name of the snippet to add")
    parser_a.add_argument(
        "--src",
        type=Path,
        required=True,
        help="Path to the text file containing the snippet body",
    )
    parser_a.add_argument(
        "--desc", type=str, help="Description of the snippet", default=""
    )

    parser_b = subparsers.add_parser("remove")
    parser_b.add_argument("name", type=str, help="Name of the snippet to remove")

    subparsers.add_parser("list")

    parser_c = subparsers.add_parser("show")
    parser_c.add_argument("name", type=str, help="Name of the snippet to show")

    return parser.parse_args()


def _add_snippet(name: str, desc: str, src: Optional[Path]):
    if src is None:
        print("! src path for command 'add' is missing")
    elif not src.is_file():
        print("! src path for command 'add' is not a file")
    else:
        with src.open("r", encoding="utf-8") as file:
            snippet_body = [line.rstrip("\n") for line in file]

        if name in data:
            print(f"! Snippet '{name}' already exists")
            exit(1)

        data[name] = {
            "prefix": name,
            "body": snippet_body,
            "description": desc,
        }

        _write_data()


def _show_snippet(name: str):
    if name not in data:
        print(f"! Snippet '{name}' does not exist")
        exit(1)
    print("---------- Snippet content ----------")
    print("\n".join(data[name]["body"]))
    print("-------------------------------------")


def _remove_snippet(name: str):
    if name not in data:
        print(f"! Snippet '{name}' does not exist")
        exit(1)

    _show_snippet(name)
    print("• Do you want to remove the specified snippet? (Y/n) ", end="")

    if input().lower() == "y":
        data.pop(name)
        _write_data()
    else:
        print("! Operation cancelled")
        exit(1)


def _list_snippets():
    print("• List of existing snippets:")
    mxlen = max(len(name) for name in data.keys())
    for name, value in data.items():
        print(f"    {name:<{mxlen}}      {value['description']}")


if __name__ == "__main__":
    args = _load_args()

    if args.command == "add":
        _add_snippet(args.name, args.desc, args.src)
    elif args.command == "remove":
        _remove_snippet(args.name)
    elif args.command == "list":
        _list_snippets()
    elif args.command == "show":
        _show_snippet(args.name)
