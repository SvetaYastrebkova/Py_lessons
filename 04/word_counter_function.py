def normalize_text(text: str, separators: list[str]) -> str:
    """Заменяет все разделители в тексте на пробел."""
    for sep in separators:
        text = text.replace(sep, " ")
    return text

def split_words(text: str) -> list[str]:
    """Разбивает строку на слова, убирая пустые элементы."""
    return [w for w in text.split(" ") if w]

def count_words(text: str, separators: list[str]) -> tuple[list[str], int]:
    """Возвращает список слов и их количество."""
    normalized = normalize_text(text, separators)
    words = split_words(normalized)
    return words, len(words)


# Пример использования
phrase = "Hello world!\nHow are you"
WORDS_SEPARATORS = [" ", "\n", "!"]

words, count = count_words(phrase, WORDS_SEPARATORS)

print("Words:", words)
print("Words count:", count)
