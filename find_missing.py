list1 = [1, 2, 3, 5, 6, 7, 9]
n = list1[-1]


def find_missing_number(list1):
    return[number for number in range(1, n) if number not in list1]
print(find_missing_number(list1))
