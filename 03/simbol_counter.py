phrase = "Hello world"

symbols_counter = []

for ch in phrase:
    # Проверяем, есть ли символ уже в списке
    found = False
    for item in symbols_counter:
        if item[0] == ch:
            item[1] += 1
            found = True
            break
    if not found:
        symbols_counter.append([ch, 1])

print(symbols_counter)
