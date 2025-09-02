# Входная строка
phrase = "Hello world!\nHow are you"

# Разделители слов
WORDS_SEPARATORS = [" ", "\n", "!"]

# Заменим все разделители на пробел
normalized = phrase
for sep in WORDS_SEPARATORS:
    normalized = normalized.replace(sep, " ")

# Разбиваем по пробелам и фильтруем пустые строки
words = [w for w in normalized.split(" ") if w]

print("Words:", words)
print("Words count:", len(words))
