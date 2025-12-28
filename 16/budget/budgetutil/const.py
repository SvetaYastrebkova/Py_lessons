from pathlib import Path
# Database structure:
# Базовая папка проекта (где лежит main.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# Папка для базы данных
DB_DIR = BASE_DIR / "budget_db"
DB_DIR.mkdir(parents=True, exist_ok=True)  # создаем если нет

# Полный путь к файлу базы
DB_FILE = DB_DIR / "budget.sqlite"

TABLE_CATEGORIES = "categories"
TABLE_TRANSACTIONS = "transactions"

MAIN_MENU = """Select action:
0 - Exit
1 - create DB if not exist
2 - add transaction
3 - show balance
4 - export transaction list
"""



