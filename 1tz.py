def merge_and_sort_descending(list1, list2):
    # Инициализация индексов для прохода по спискам
    i, j = len(list1) - 1, len(list2) - 1
    res = []
    
    # Пока оба индекса не вышли за пределы списков
    while i >= 0 and j >= 0:
        if list1[i] > list2[j]:
            res.append(list1[i])
            i -= 1
        else:
            res.append(list2[j])
            j -= 1
    
    # Добавляем оставшиеся элементы из list1, если есть
    while i >= 0:
        res.append(list1[i])
        i -= 1
    
    # Добавляем оставшиеся элементы из list2, если есть
    while j >= 0:
        res.append(list2[j])
        j -= 1
    
    return res

# Примеры использования:
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

result = merge_and_sort_descending(list1, list2)
print(result)  # Ожидаемый результат: [8, 7, 6, 5, 4, 3, 2, 1]
