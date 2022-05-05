#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(
        description="Compare two configuration files and show a difference.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )

parser.add_argument("first_file")
parser.add_argument("second_file")
args = parser.parse_args()
config = vars(args)


def main():
    print(config)


if __name__ == '__main__':
    main()
