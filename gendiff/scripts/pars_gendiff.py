#!/usr/bin/env python

import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compare two configuration files and show a difference.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")

    args = parser.parse_args()
    config = vars(args)
    return args
