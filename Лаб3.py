stuffdict = {'в': (3, 25), 'п': (2, 15), 'б': (2, 15), 'а': (2, 20), 'и': (1, 5), 'н': (1, 15), 'т': (3, 20),
             'о': (1, 25), 'ф': (1, 15), 'д': (1, 10), 'к': (2, 20), 'р': (2, 20)}


def get_area_and_value(stuffdict):
    area = [stuffdict[item][0] for item in stuffdict]
    value = [stuffdict[item][1] for item in stuffdict]
    return area, value

summ = 0
for q in stuffdict.values():
    summ += int(q[1])

def get_memtable(stuffdict, A=9):
    area, value = get_area_and_value(stuffdict)
    n = len(value)

    V = [[0 for a in range(A+1)] for i in range(n+1)]

    for i in range(n + 1):
        for a in range(A + 1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif area[i - 1] <= a:
                V[i][a] = max(value[i - 1] + V[i - 1][a-area[i-1]], V[i-1][a])
            else:
                V[i][a] = V[i - 1][a]
    return V, area, value

def get_result(stuffdict, A=9):
    V, area, value, = get_memtable(stuffdict)
    n = len(value)
    res = V[n][A]
    return res

def get_selected_items_list(stuffdict, A=9):
    V, area, value, = get_memtable(stuffdict)
    n = len(value)
    res = V[n][A]
    a = A
    items_list = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == V[i - 1][a]:
            continue
        else:
            items_list.append((area[i - 1], value[i - 1]))
            res -= value[i - 1]
            a -= area[i - 1]

    selected_stuff = []

    for search in items_list:
        for key, value in stuffdict.items():
            if value == search:
                selected_stuff.append(key)

    return selected_stuff

stuff = get_selected_items_list(stuffdict)


list_repetitions = []

for x in stuff:
    if x not in list_repetitions:
        list_repetitions.append(x)
    stuff = list_repetitions

list_end = []
for y in stuff:
    for z in range(stuffdict[y][0]):
        list_end.append(list(y))


result = (get_result(stuffdict, A=9))
no_selected = summ - result
result -= no_selected
result += 15

print(list_end)
print(result)



