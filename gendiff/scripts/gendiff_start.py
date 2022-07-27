#!/usr/bin/env python

import os
import json
import pars_gendiff
import yaml

args = pars_gendiff.parse_args()

first_file_path = args.first_file
second_file_path = args.second_file

def read_file_data(file_path):
    if file_path.lower().endswith(".yml") or first_file_path.lower().endswith(".yaml"):
        with open((file_path), "r") as stream:
            data = yaml.safe_load(stream)
    elif file_path.lower().endswith(".json"):
        data = json.load(open((file_path), "r"))
    else:
        raise TypeError("Wrong file format. Support only JSON or YAML")
    return data

first_file_data = read_file_data(first_file_path)
second_file_data = read_file_data(second_file_path)


def formated_value(var):
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
            diff = diff + '  - ' + key + formated_value(merged_dict[key])
        elif key not in first_dict:
            diff = diff + '  + ' + key + formated_value(merged_dict[key])
        elif first_dict[key] == second_dict[key]:
            diff = diff + '    ' + key + formated_value(merged_dict[key])
        else:
            diff = diff + '  - ' + key + formated_value(first_dict[key])
            diff = diff + '  + ' + key + formated_value(second_dict[key])
    diff = diff + '}'
    result_file = open(os.path.join(os.getcwd(), 'result.txt'), "w+")
    result_file.write(diff)
    result_file.close
    return diff


def main():
    print(generate_diff(first_file_data, second_file_data))


if __name__ == '__main__':
    main()
