symbols = list(input("Enter something: "))

second_symbol = None
first_symbol = None
suffix_symbols = []

match symbols:
    # Первый вариант: первый символ a, b или c
    case [("a" | "b" | "c") as first_symbol, *suffix_symbols]:
        print("First case")
    
    # Второй вариант: первый символ d, второй — буква ASCII A–Z
    case ["d" as first_symbol, second_symbol, *suffix_symbols] if ord(second_symbol) in range(65, 91):
        print("Second case")
    
    # Третий вариант: первый символ d, второй любой
    case ["d" as first_symbol, second_symbol, *suffix_symbols]:
        print("Third case")

print("type(suffix_symbols):", type(suffix_symbols))
print("suffix_symbols:", suffix_symbols)
print("first_symbol:", first_symbol)
print("second_symbol:", second_symbol)