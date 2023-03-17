"""Argparse snippets."""
import argparse
import pathlib


def main() -> None:
    """Main method."""
    parser = argparse.ArgumentParser()
    parser.add_argument("count", type=int)
    parser.add_argument("distance", type=float)
    parser.add_argument("street", type=ascii)
    parser.add_argument("code_point", type=ord)
    parser.add_argument("source_file", type=open)
    parser.add_argument("dest_file", type=argparse.FileType("w", encoding="latin-1"))
    parser.add_argument("datapath", type=pathlib.Path)
    parser.add_argument("--opt", help="opt help")
    parser.add_argument("--flag", destination="check", action="store_true")
    parser.add_argument("--no-flag", destination="check", action="store_false")

    args = parser.parse_args()
    print(args.arg)
    if args.opt:
        print(args.opt)

    print(args.check)


if __name__ == "__main__":
    main()
