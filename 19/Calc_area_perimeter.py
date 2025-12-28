# Calc area, perimeter
def shapes_calc(shape):
    PI = 3.1415926

    if shape == 's':  # квадрат
        def square(side):
            area = side * side
            perimeter = 4 * side
            return area, perimeter
        return square

    elif shape == 'r':  # прямоугольник
        def rectangle(length, width):
            area = length * width
            perimeter = 2 * (length + width)
            return area, perimeter
        return rectangle

    elif shape == 'c':  # круг
        def circle(radius):
            area = PI * radius * radius
            perimeter = 2 * PI * radius
            return area, perimeter
        return circle

    else:
        raise ValueError("Unknown shape. Use 's' for square, 'r' for rectangle, 'c' for circle.")

# Примеры использования

calc_squares = shapes_calc('s')
#calc_squares(10)
print (calc_squares(10))

calc_rectangles = shapes_calc('r')
#calc_rectangles(10,6)
print(calc_rectangles(10,6))

calc_circles = shapes_calc('c')
#calc_circles(7)
print(calc_circles(7))