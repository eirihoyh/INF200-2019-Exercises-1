# -*- coding: utf-8 -*-

__author__ = 'Erik Rullestad'
__email__ = 'erikrull@nmbu.no'

import statistics as stats
import pytest


def median(data):
    """This code is copied from "exercise 3" and is made by Yngve Moe.
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """
    sdata = sorted(data)
    n = len(sdata)
    if n == 0:
        raise ValueError('The list must be of minimum length 1')
    return (sdata[n // 2] if n % 2 == 1
            else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


def test_median_one_element_list():
    """A test that checks if the function returns the correct value for a
    one-element list."""
    data = [1]
    assert median(data) == stats.median(data)


def test_median_different_lists():
    """ A tests that the median-function returns correct values for:
    - Lists with odd number of elements
    - Lists with even number of elements
    - Ordered lists
    - Reverse-ordered list
    - Unordered list
    """
    for data in [[1, 2, 3, 4, 5],
                 [1, 2, 3, 4, 5, 6],
                 [5, 4, 3, 2, 1],
                 [2, 5, 1, 3, 4]]:
        assert median(data) == stats.median(data)


def test_raises_value_error():
    """A test that raises "ValueError" if the list is empty"""
    empty_list = []
    with pytest.raises(ValueError):
        assert median(empty_list)


def test_original_data_unchanged():
    """A test that checks if the function leaves the original data
    unchanged"""
    original_data = [5, 3, 1, 4, 2]
    median_data = median(original_data)
    assert median_data != original_data
    assert original_data == [5, 3, 1, 4, 2]


def test_tuples_and_lists():
    """A test that checks if the function works for both tuples and lists"""
    data = (3, 6, 88, 7, 101, 13, 65, 5)
    assert median(data) == median(list(data))
