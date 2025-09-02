# Запрашиваем максимальное число
n = int(input("Введите число: "))

# Создаём таблицу умножения в виде кортежа кортежей
mult_table = tuple(
    tuple(i * j for j in range(1, n + 1))
    for i in range(1, n + 1)
)

# Печатаем таблицу
for row in mult_table:
    print(row)
