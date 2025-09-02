# STEP 1: define constants (colors)
SOURCE_HTML = '''
<h1>My First Heading</h1>
<h2>My second Heading</h2>
<p>My first paragraph.</p>
<h1>My Heading 3</h1>
<p>My paragraph 2</p>
'''

RESET_COLORS = "\033[0m"
COLOR_RED = "\033[38;5;196m"    
COLOR_YELLOW = "\033[38;5;226m"  
COLOR_GREEN = "\033[38;5;46m"

HTML_TAGS = [
    ["h1", COLOR_RED],
    ["h2", COLOR_YELLOW],
    ["p", COLOR_GREEN],
]

# STEP 2: parse HTML text manually
html_tokens = []
search_start = 0

while True:
    tag_open = SOURCE_HTML.find("<", search_start)
    if tag_open == -1:
        break

    tag_close = SOURCE_HTML.find(">", tag_open)
    if tag_close == -1:
        break

    # имя тега
    tag_name = SOURCE_HTML[tag_open+1:tag_close].strip("/")

    # ищем закрывающий тег
    closing_tag = f"</{tag_name}>"
    tag_end = SOURCE_HTML.find(closing_tag, tag_close)
    if tag_end == -1:
        break

    # содержимое
    token_text = SOURCE_HTML[tag_close+1:tag_end]

    html_tokens.append([tag_name, token_text.strip()])

    search_start = tag_end + len(closing_tag)

# STEP 3: print result (colorized)
for tag, text in html_tokens:
    color = RESET_COLORS
    for t, c in HTML_TAGS:
        if t == tag:
            color = c
            break
    print(color + text + RESET_COLORS)
