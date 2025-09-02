def print_rectangle(width: int, height: int, symbol: str):
    """Рисует прямоугольник из символов."""
    for _ in range(height):
        print(symbol * width)


# Пример использования
width = 7
height = 2
symbol = "*"

print_rectangle(width, height, symbol)
