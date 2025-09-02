def print_colored_rectangle(width: int, height: int, border: int, border_symbol="R", inner_symbol="b"):
    """Рисует прямоугольник с рамкой (border) и внутренней заливкой."""
    total_width = width + 2 * border
    total_height = height + 2 * border

    for row in range(total_height):
        line = ""
        for col in range(total_width):
            # Условие: рамка или внутренняя часть
            if (row < border or row >= total_height - border or
                col < border or col >= total_width - border):
                line += border_symbol
            else:
                line += inner_symbol
        print(line)


# Пример использования
width = 6
height = 4
border = 1

print_colored_rectangle(width, height, border)
