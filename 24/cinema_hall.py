# Cinema hall:
'''

3    000101100000110000000000000
2    000000000000000000000000000
1    111111111111111111111111111
    
     _________ SCREEN __________
     
     
Cinema management functions:
- cell ticket
- print cinema hall
- return ticket
- check free places

'''

# Кинотеатр: каждый ряд — список символов '0' и '1'
cinema = [
    list("111111111111111111111111111"),   # ряд 1
    list("000000000000000000000000000"),  # ряд 2
    list("000101100000110000000000000")   # ряд 3
]

def print_hall():
    """Печатает схему зала"""
    print()
    for i in range(len(cinema)-1, -1, -1):  # от последнего ряда к первому
        print(f"{i+1:>2}   {''.join(cinema[i])}")
    print("\n     _________ SCREEN __________\n")



def check_free_places():
    """Показывает количество свободных мест"""
    print("\nСвободные места по рядам:")
    for i, row in enumerate(cinema, start=1):
        free = row.count('0')
        print(f"Ряд {i}: свободно {free} мест")
    print()

def sell_ticket(row, seat):
    """Продаёт билет"""
    try:
        row_idx = row - 1
        seat_idx = seat - 1
        if cinema[row_idx][seat_idx] == '0':
            cinema[row_idx][seat_idx] = '1'
            print(f"Билет продан: ряд {row}, место {seat}")
        else:
            print(f"Место {seat} в ряду {row} уже занято!")
    except IndexError:
        print("Некорректный номер ряда или места!")

def return_ticket(row, seat):
    """Возвращает билет"""
    try:
        row_idx = row - 1
        seat_idx = seat - 1
        if cinema[row_idx][seat_idx] == '1':
            cinema[row_idx][seat_idx] = '0'
            print(f"Билет возвращён: ряд {row}, место {seat}")
        else:
            print(f"Место {seat} в ряду {row} уже свободно.")
    except IndexError:
        print("Некорректный номер ряда или места!")

def menu():
    """Главное меню"""
    while True:
        print("""
 Меню кинотеатра:
1. Показать зал
2. Проверить свободные места
3. Купить билет
4. Вернуть билет
5. Выйти
""")
        choice = input("Выберите действие: ")

        if choice == '1':
            print_hall()
        elif choice == '2':
            check_free_places()
        elif choice == '3':
            row = int(input("Введите номер ряда: "))
            seat = int(input("Введите номер места: "))
            sell_ticket(row, seat)
        elif choice == '4':
            row = int(input("Введите номер ряда: "))
            seat = int(input("Введите номер места: "))
            return_ticket(row, seat)
        elif choice == '5':
            print(" До свидания!")
            break
        else:
            print(" Неверный выбор, попробуйте снова.")

# --- Запуск ---
menu()