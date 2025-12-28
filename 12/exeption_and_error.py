try:
    x = [1, 2, 3]
    print(x[5])
except ZeroDivisionError:
    print("Error")
except :
    print("Error")
else:
    print("Else  block")
finally:
    print("Done")

print('After try - except')

list1 = []


# AssertionError: ERROR empty list!
try:
    assert len(list1) != 0, "ERROR empty list!"  # проверка: список не пустой
    print("List is OK")
except AssertionError as e:
    print("AssertionError:", e)
