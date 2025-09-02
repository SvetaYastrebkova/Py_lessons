#py copy module

import copy 

list1 = [
    [1,2,3],
    [11,22,33],
    [111,222,333]
]

list2_shallow = copy.copy(list1)
print(id(list1))
print(id(list2_shallow))

#хранение списка ссылок на один и теже дочки

print()
for e in list1:
    print(f'list1 children: {id(e)}')
    pass

for e in list2_shallow:
    print(f'list2_shallow children: {id(e)}')
    pass

#пример с месяцами 


months_en = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months_ru = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
months_he = ["ינואר", "פברואר", "מרץ", "אפריל", "מאי", "יוני", "יולי", "אוגוסט", "ספטמבר", "אוקטובר", "נובמבר", "דצמבר"]

months_multilang = [
    1,
    months_en,
    2,
    months_ru,
    3,
    months_he 
]

month_shallow = copy.copy(months_multilang)
print(months_multilang)
print(id(months_multilang))
print(month_shallow)
print(id(month_shallow))
months_multilang[0] = 222
months_en[0] = None
print(10* "*")
print(months_multilang)
print(id(months_multilang))
print(month_shallow)
print(id(month_shallow))

# deep copy

list1 = [
    100,
    [11,22,33]
]

list2 = list1.copy()

print(list1)
print(list2)

list1[0] = 999
print(list1)
print(list2)

list1[1][0] = 123455
print(list1)
print(list2)

#deep copy
# Deep copy, shallow copy

list1 = [
    100,
    [11,22,33]
]

list2 = copy.copy(list1)
list3 = copy.deepcopy(list1)
print("Before changes:")
print(list1)
print(list2)
print(list3)
print("Change list1[0]")
list1[0] = 999
print(list1)
print(list2)
print(list2)
print("Change list1[1][0]")
list1[1][0] = 12345
print(list1)
print(list2)
print(list2)

