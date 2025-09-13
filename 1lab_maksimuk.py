#объединяем два словаря, суммируя значения одинаковых ключей
def merge_dicts(d1, d2):
    #создаем копию первого словаря, чтобы не изменять исходные значения
    result = d1.copy()
    for key, value in d2.items():
        #существует ли текущий ключ уже в результирующем словаре
        if key in result:
            result[key] += value
        else:
            result[key] = value
            #возвращаем обединенный словарь
    return result
d1 = {'a':200, 'b':50}
d2 = {'a':100, 'c':500}
print(merge_dicts(d1, d2))
