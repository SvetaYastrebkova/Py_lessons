from budgetutil import init_db

from budgetutil.const import MAIN_MENU
from budgetutil.budget_util import add_transaction, get_balance, export_transactions
from datetime import datetime

def main():
    while True:
        print(MAIN_MENU)
        choice = input("Enter choice: ")

        if choice == "0":
            print("Exiting...")
            break

        elif choice == "1":
            init_db()
            print("Database initialized.")

        elif choice == "2":
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            amount = float(input("Enter amount: "))
            sign = input("Enter sign (+/-): ").strip()
            category = input("Enter category: ").strip()
            comment = input("Enter comment: ").strip()
            add_transaction(date, amount, sign, category, comment)
            print("Transaction added.")

        elif choice == "3":
            balance = get_balance()
            print(f"Current balance: {balance}")

        elif choice == "4":
            filename = export_transactions()
            print(f"Transactions exported to {filename}")

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
