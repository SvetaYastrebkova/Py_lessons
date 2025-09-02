# format
# loops
# func pars
# 

numbers = [
    [1,2,33,-4],
    [1,2,3,4,22,33,44,-1],
    [1,2,3,4,3,11,-3,987],
]

counter = 0
for row in numbers:
    for item in row:
        counter += 1
        if item < 0 :
            break # если элемент < 0, выполняется break из внутреннего цикла
        pass
    else: #выполняется только если внутренний цикл завершился без break
        continue
    break


print(f"counter = {counter}")