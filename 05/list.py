#python list com

list1 = [i for i in range(10)]
print(list1)

letters = [chr(i) for i in range (97,123)]
print(letters)

letters = [[chr(i), f"{i:04X}"] for i in range (97,123)]
print(letters)


# степени
numbers = [
    [ j**i for j in range(10)]
      for i in range (4)
      ]
print(numbers)


#четный ряд
nums = [
    i for i in range(100) if i%2 == 0
]
print(nums)

def new_item(loop_var):
    return (loop_var*100)
print([new_item(i) for i in range(10)])