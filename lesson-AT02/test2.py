import pytest
from main2 import check_even, is_palindrome, sort_list


def test_check_even():
    assert check_even(6) == True


def test_check_even2():
    assert check_even(7) == False


@pytest.mark.parametrize('number, expected', [
    (2, True),
    (5, False),
    (0, True),
    (56, True),
    (-3, False)
])
def test_check_even_with_params(number, expected):
    assert check_even(number) == expected


def test_is_palindrome_true():
    assert is_palindrome('madam') == True


def test_is_palindrome_false():
    assert is_palindrome('hello') == False


@pytest.mark.parametrize('word, expected', [
    ('level', True),
    ('python', False),
    ('racecar', True),
    ('', True),
])
def test_is_palindrome_with_params(word, expected):
    assert is_palindrome(word) == expected


def test_sort_list1():
    assert sort_list([5, 6, 3, 1, 2]) == [1, 2, 3, 5, 6]


def test_sort_list2():
    assert sort_list([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]
    