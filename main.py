import sys
import pdb
import argparse
import controller


def func_update(args: argparse.Namespace):
    print("Update:")
    print(args)
    controller.update(args.dir)


def func_init(args: argparse.Namespace):
    print("init")


def main():
    parser = argparse.ArgumentParser(prog="main.py")
    subparsers = parser.add_subparsers(help="subcommands")

    parser_init = subparsers.add_parser('init', help='initialize a repo')
    parser_init.set_defaults(func=func_init)

    parser_update = subparsers.add_parser('update', help='update a directory')
    parser_update.add_argument('dir', help='dir to update')
    parser_update.set_defaults(func=func_update)

    args = parser.parse_args(sys.argv[1:])  # the first argument is main.py
    args.func(args)


if __name__ == "__main__":
    main()
