#!/usr/bin/env python

from asyncore import read

def test_result():
    expected_result = open("gendiff/tests/fixtures/expected_result.txt", "r").read()
    result = open("gendiff/result.txt", "r").read()
    assert result == expected_result


if __name__ == '__main__':
    main()