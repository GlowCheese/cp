import argparse
import json
from pathlib import Path
from typing import Optional


def load_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    parser_a = subparsers.add_parser("add")
    parser_a.add_argument("name", type=str, help="Name of the snippet")
    parser_a.add_argument(
        "--src",
        type=Path,
        required=True,
        help="Path to the text file containing the snippet body",
    )
    parser_a.add_argument(
        "--desc", type=str, help="Description of the snippet", default=""
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = load_args()

    if args.command == "add":
        src: Optional[Path] = args.src
        if src is None:
            print("! src path for command 'add' is missing")
        elif not src.is_file():
            print("! src path for command 'add' is not a file")
        else:
            with src.open("r", encoding="utf-8") as file:
                snippet_body = [line.rstrip("\n") for line in file]

            json_path = Path(".helix/snippets/cpp.json")

            if not json_path.exists():
                data = {}
            else:
                with json_path.open("r", encoding="utf-8") as file:
                    data = json.load(file)

            if args.name in data:
                print(f"! Snippet '{args.name}' already exists")
                exit(1)

            data[args.name] = {
                "prefix": args.name,
                "body": snippet_body,
                "description": args.desc,
            }

            with json_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
