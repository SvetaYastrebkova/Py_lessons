# Базовые ANSI-коды
RESET = "\033[0m"
# console_colors/ansi.py

# Сброс всех атрибутов
RESET = "\033[0m"

# Пять основных цветов текста (переднего плана)
RED   = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE  = "\033[34m"
CYAN  = "\033[36m"


def color(text: str, color_code: str) -> str:
    """
    Окрашивает строку в выбранный цвет.
    
    :param text: строка для вывода
    :param color_code: ANSI-код цвета (например RED, GREEN)
    :return: окрашенная строка
    """
    return f"{color_code}{text}{RESET}"