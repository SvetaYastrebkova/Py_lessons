import re

# HTML-текст
html_text = """
<h1>heading 1 text</h1>
<p>paragraph 1</p>
"""

# ANSI-цвета
COLOR_RED = "\033[31m"
COLOR_YELLOW = "\033[33m"
COLOR_GREEN = "\033[32m"
RESET = "\033[0m"

# Теги и цвета
HTML_TAGS = [
    ["h1", COLOR_RED],
    ["h2", COLOR_YELLOW],
    ["p", COLOR_GREEN],
]

colored_text = html_text

# Заменяем теги на цвета
for tag, color in HTML_TAGS:
    colored_text = re.sub(fr"<{tag}>", color, colored_text)
    colored_text = re.sub(fr"</{tag}>", RESET, colored_text)

print(colored_text)
