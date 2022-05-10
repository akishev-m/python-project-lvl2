#!/usr/bin/env python

import argparse
import json
import pprint

parser = argparse.ArgumentParser(
        description="Compare two configuration files and show a difference.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )

parser.add_argument("first_file")
parser.add_argument("second_file")
parser.add_argument("-f", "--format", help="set format of output")

args = parser.parse_args()
config = vars(args)


first_file = args.first_file
second_file = args.second_file

first_f = json.load(open((first_file), "r"))
second_f = json.load(open((second_file), "r"))


def make_addition(var):
    if isinstance(var, bool):
        if var:
            return ': true\n'
        else:
            return ': false\n'
    else:
        return ': ' + str(var) + '\n'


def generate_diff(first_dict, second_dict):
    merged_dict = {**first_dict, **second_dict}
    diff = '{\n'
    for key in sorted(merged_dict.keys()):
        if key not in second_dict:
            diff = diff + '  - ' + key + make_addition(merged_dict[key])
        elif key not in first_dict:
            diff = diff + '  + ' + key + make_addition(merged_dict[key])
        elif first_dict[key] == second_dict[key]:
            diff = diff + '    ' + key + make_addition(merged_dict[key])
        else:
            diff = diff + '  - ' + key + make_addition(first_dict[key])
            diff = diff + '  + ' + key + make_addition(second_dict[key])
    diff = diff + '{'
    return diff


def main():
    print(first_file)
    pprint.pprint(first_f, width=40)
    print(second_file)
    pprint.pprint(second_f, width=40)
    print('Difference')
    print(generate_diff(first_f, second_f))


if __name__ == '__main__':
    main()
