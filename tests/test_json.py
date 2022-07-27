#!/usr/bin/env python

import os

def test_json():
    expected_result = open(os.path.join(os.getcwd(), 'tests', 'fixtures', 'expected_json.txt'), "r").read()
    result = open(os.path.join(os.getcwd(), 'result.txt'), "r").read()

    assert result == expected_result


def main():
    test_json()


if __name__ == '__main__':
    main()