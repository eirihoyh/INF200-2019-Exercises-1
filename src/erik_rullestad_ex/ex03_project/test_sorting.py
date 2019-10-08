# -*- coding: utf-8 -*-

__author__ = 'Erik Rullestad'
__email__ = 'erikrull@nmbu.no'


def bubble_sort(data):
    len_data = len(data) - 1
    data = list(data)
    for i in range(len_data):
        for j in range(len_data - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def test_empty():
    """Test that the sorting function works for empty list"""
    empty_list = []
    assert bubble_sort(empty_list) == empty_list


def test_single():
    """Test that the sorting function works for single-element list"""
    single_list = [1]
    assert bubble_sort(single_list) == single_list


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data != sorted_data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data != sorted_data
    assert data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    pre_sorted_data = [1, 2, 3, 4, 5]
    assert bubble_sort(pre_sorted_data) == pre_sorted_data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    reversed_sorted_data = [5, 4, 3, 2, 1]
    assert bubble_sort(reversed_sorted_data) == sorted(reversed_sorted_data)


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    identical_elements = [5, 2, 3, 7, 8, 7, 5, 4, 1, ]
    assert bubble_sort(identical_elements) == sorted(identical_elements)


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    for data in [(1, 6, 5, 3, 4, 2),
                 ('hello', '27', 'a', 'x', '7'),
                 [22, 88, 44, 66, 77, 55],
                 ['This', 'is', 'a', 'test', '!']]:
        assert list(bubble_sort(data)) == sorted(data)
