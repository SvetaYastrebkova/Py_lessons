#recursion

'''
Рекурсия — это когда функция вызывает сама себя. Используется, чтобы решать задачи, которые естественно разбиваются на похожие подзадачи (например, дерево вызовов, обход структур, деление задачи пополам).

Ключевые элементы рекурсии:

Базовый случай (base case) — условие, при котором функция возвращает результат без рекурсивного вызова. Без него будет бесконечная рекурсия и RecursionError.

Рекурсивный шаг — вызов функции с «меньшей» (более простой) версией задачи.
'''

#факториал

def factorial(n):
    # базовый случай
    if n <= 1:
        return 1
    # рекурсивный шаг
    return n * factorial(n - 1)

print(factorial(5))  # 120


#фибоначи 
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print([fib(i) for i in range(12)])  # [0,1,1,2,3,5,8,13,21,34]

# граф 

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

def count_edges(graph):
    visited = set()
    edges = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            # добавляем ребро как неупорядоченное множество (frozenset)
            edges.add(frozenset([node, neighbor]))
            if neighbor not in visited:
                dfs(neighbor)

    # стартуем с первой вершины
    start_node = next(iter(graph))
    dfs(start_node)

    return len(edges)


# Пример
print(count_edges(graph))  # 4



# Lists 
# 
lst1 = [1,[1,2,3],[1,[1,2]],[1,2,[1,2]]]

def recursive_sum_nested_list(lst1):
    sum_total = 0
    for item in lst1:
        if isinstance(item, list):  # если элемент — список, вызываем рекурсию
            sum_total += recursive_sum_nested_list(item)
        else:  # если число, прибавляем напрямую
            sum_total += item
    return sum_total

print(recursive_sum_nested_list(lst1))

# пример
#l1 = [1, [1, 2, 3], [1, [1, 2]]]
#print(recursive_sum_nested_list(l1))  # 👉 11

lst1 = [1, [1, 2, 3], [1, [1, 2]], [1, 2, [1, 2,[1,2]]]]

def recursive_sum_nested_list(lst1):
    sum_total = 0
    for item in lst1:
        if type(item) == list:  # проверка типа через type()
            sum_total += recursive_sum_nested_list(item)
        else:
            sum_total += item
    return sum_total

print(recursive_sum_nested_list(lst1))
