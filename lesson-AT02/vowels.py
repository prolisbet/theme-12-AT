import pytest


def count_vowels(string):
    count = 0
    for symbol in string.lower():
        if symbol in 'aeiouyаеёиоуыэюя':
            count += 1
    return count


def test_count_vowels():
    assert count_vowels('hello') == 2
    assert count_vowels('привет') == 2
    assert count_vowels('this is python') == 4


def test_count_vowels_not():
    assert count_vowels('version control') != 3
    assert count_vowels('это все питон') != 3
    assert count_vowels('hello world') != 2


def test_count_vowels_only():
    assert count_vowels('aaaaaaaa') == 8


def test_count_vowels_none():
    assert count_vowels('brbrbrbr') == 0


def test_count_vowels_register():
    assert count_vowels('Изучим мокирование и тестирование API.') == 18


@pytest.mark.parametrize('string, expected', [
    ('До свидания', 5),
    ('Au revoir', 5),
    ("c'est un moment incroyable", 9),
    ('eau', 3),
    ('Ау!!!', 2),
    ('прст', 0),
    ('Съешь Ещё Этих Мягких Французских Булок, Да Выпей Же Чаю', 18)
])
def test_count_vowels_with_params(string, expected):
    assert count_vowels(string) == expected
