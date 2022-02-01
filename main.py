points = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)] #список координат

#функция нахождения растояния двух точек
def route_(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5

#функция возвращает строку с координатами и промежуточными расстояниями
def key(list):
    a = route_(points[0], list[0])
    b = a + route_(list[0], list[1])
    c = b + route_(list[1], list[2])
    d = c + route_(list[2], list[3])
    n = d + route_(list[3], points[0])
    return f"{points[0]} -> {list[0]} [{a}] -> {list[1]} [{b}] -> {list[2]} [{c}] -> {list[3]} [{d}] ->/" \
           f" {points[0]} [{n}] = {n}"

res = {}

#цикл перебирает все возможные варианты прохождения по пунктам
for i in range(1, 5):
    for j in range(1, 5):
        if j == i:
            continue
        for k in range(1, 5):
            if i == k or j == k:
                continue
            for a in range(1, 5):
                if i == a or j == a or k == a:
                    continue
                #находим расстояние между пунктами и суммируем
                route = route_(points[0], points[i]) + route_(points[i], points[j]) + route_(points[j], points[k])\
                + route_(points[k], points[a]) + route_(points[a], points[0])
                #записываем координаты в словарь, ключ - пройденное расстояние
                res[route] = [points[i],  points[j], points[k], points[a]]

#сортируем словарь по возрастанию ключей
keys = sorted(res.keys())

#цикл перебирает ключи словаря, на каждой итерации печатает информацию о пройденом маршруте
for i in keys:
    print(key(res[i]))
    print()
