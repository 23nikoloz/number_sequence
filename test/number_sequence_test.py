import core.number_sequence


def print_test(name, data):
    print(name)
    print("data:" + str(data))
    print(core.number_sequence.find_sequence(data))
    print("-------------------------------------")


print_test("test 1", range(0, 10))

print_test("test 2", [1, 2, 3, 5, 6, 7, 9, 10])
