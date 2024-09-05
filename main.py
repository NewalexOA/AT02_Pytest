import pytest

def count_vowels(string):
    """
    Подсчитывает количество гласных букв в заданной строке.
    Учитывает как английские, так и русские гласные, независимо от регистра.
    """
    vowels = 'aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ'
    return sum(1 for char in string if char in vowels)

@pytest.mark.parametrize("input_string, expected_count", [
    ('aeiouаеёиоуыэюяАЕЁИОУЫЭЮЯ', 25),  # Все гласные (английские и русские)
    ('bcdfg', 0),                        # Строка без гласных
    ('Hello, World!', 3),                # Смешанная строка
    ('aEiOuаеёиоуыэюяАЕЁИОУЫЭЮЯ', 25),   # Проверка регистронезависимости
    ('', 0),                             # Пустая строка
    ('аеёиоуыэюяАЕЁИОУЫЭЮЯ', 20),        # Только русские гласные
    ('aеёиоуыэюяАЕЁИОУЫЭЮЯ', 20),        # Смесь английских и русских гласных
])

def test_count_vowels(input_string, expected_count):
    """
    Параметризованный тест для функции count_vowels.
    Проверяет различные сценарии входных данных.
    """
    assert count_vowels(input_string) == expected_count

# Дополнительный тест для проверки типа возвращаемого значения
def test_return_type():
    """
    Проверяет, что функция count_vowels возвращает целое число.
    """
    assert isinstance(count_vowels("test"), int)
