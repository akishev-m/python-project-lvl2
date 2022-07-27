#!/usr/bin/env python

import json
import parsing
import yaml
import pprint

args = parsing.parse_args()

first_file = args.first_file
second_file = args.second_file

with open((first_file), "r") as stream:
    first_f = yaml.safe_load(stream)

with open((second_file), "r") as stream:
    second_f = yaml.safe_load(stream)

def check(first_file):
    if first_file.endswith(".yml") or first_file.endswith(".yaml"):
        print('yes')
    else:
        print('no')


def main():
    print(check(first_file))


if __name__ == '__main__':
    main()
