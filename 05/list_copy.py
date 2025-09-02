#list copy

num1 = [1,2,3,4,5]
num2 = num1

print(num1)
print(num2)

num1[0] = 22222
print(num1)
print(num2)
print(id(num1))
print(id(num2))

num3 = num1[:]
print(id(num3))

num1[0] = 9999
print(num1)
print(num2)
print(num3)


print(id(num1))
num1 = []
print(id(num1))
#py copy module

