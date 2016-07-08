def find_sequence(indexes):
    result = {}

    sorted(indexes)

    start = -1
    count = 1

    list_size = len(indexes)

    for i in range(list_size + 1):
        if i == 0:
            start = indexes[i]
        elif i == list_size:
            result[start] = count
        else:
            if indexes[i - 1] + 1 == indexes[i]:
                count += 1
            else:
                result[start] = count
                count = 1
                start = indexes[i]

    return result
