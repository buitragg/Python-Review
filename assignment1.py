# Name: Gian M Buitrago
# OSU Email: buitragg@oregonstate.edu
# Course:       CS261 - Data Structures
# Assignment: Python Review
# Due Date: 7/05/22
# Description:


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> (int, int):
    """
    TODO: Write this implementation
    """

    minimum = arr[0]
    maximum = arr[0]

    for number in range(arr.length()):
        minimum = min(minimum, arr[number])
        maximum = max(maximum, arr[number])

    return minimum, maximum


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """

    result = StaticArray(arr.length())

    for number in range(arr.length()):
        num = arr[number]
        if num % 3 == 0 and num % 5 == 0:
            result[number] = "fizzbuzz"
        elif num % 3 == 0:
            result[number] = "fizz"
        elif num % 5 == 0:
            result[number] = "buzz"
        else:
            result[number] = arr[number]
    return result


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    TODO: Write this implementation
    """
    first = 0
    last = arr.length() - 1
    while first < last:
        num = arr.get(first)
        arr.set(first, arr.get(last))
        arr.set(last, num)
        last -= 1
        first += 1
    return


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass

    index_number = arr.length()
    steps = (steps % index_number + index_number) % index_number
    new_arr = StaticArray(index_number)
    for numbers in range(index_number):
        new_arr[numbers] = arr[(numbers - steps + index_number) % index_number]

    return new_arr


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    sa = StaticArray(abs(end - start) + 1)
    increasing = end > start
    index = 0
    some_number = start
    while some_number != end:
        sa.set(index, some_number)
        index += 1
        if increasing:
            some_number += 1
        else:
            some_number -= 1
    sa.set(index, some_number)
    return sa


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    TODO: Write this implementation
    """
    if arr.length() == 1:
        return 1
    else:
        order = 0
        for number in range(arr.length() - 1):
            val1 = arr.get(number)
            val2 = arr.get(number + 1)

            if number == 0:
                if val1 > val2:
                    order = -1
                elif val1 < val2:
                    order = 1
            else:
                if order == -1:
                    if val1 <= val2:
                        return 0
                elif order == 1:
                    if val1 >= val2:
                        return 0
        return order


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """
    TODO: Write this implementation
    """
    max = arr[0]
    max_count = 1
    temp_count = 1
    temp = arr[0]

    for data in range(1, arr.length()):
        if arr[data] == temp:
            temp_count += 1
        else:
            if temp_count > max_count:
                max_count = temp_count
                max = temp

            temp = arr[data]
            temp_count = 1

    return max, max_count


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    new_array = StaticArray(arr.length())
    total_values = 1
    new_array[0] = arr[0]
    for number in range(1, new_array.length()):
        if not arr[number] == arr[number - 1]:
            total_values += 1
            new_array[number] = arr[number]
    final_array = StaticArray(total_values)
    final_index = 0
    for number in range(new_array.length()):
        if new_array[number] is not None:
            final_array[final_index] = new_array[number]
            final_index += 1
    return final_array






# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    max = -int(10 ** 100)
    min = int(10 ** 100)
    for number in range(arr.length()):
        if max < arr.get(number):
            max = arr.get(number)
        if min > arr.get(number):
            min = arr.get(number)
    max = max - min
    max += 1
    count = StaticArray(max)
    for number in range(max):
        count[number] = 0
    for number in range(arr.length()):
        value = count.get(arr.get(number) - min)
        count.set(arr.get(number) - min, value + 1)
    for number in range(1, max):
        count.set(number, count.get(number) + count.get(number - 1))
    output = StaticArray(arr.length())
    number = arr.length() - 1
    while number >= 0:

        output.set(arr.length() - number - 1, arr.get(number))
        count.set(arr.get(number) - min, count.get(arr.get(number) - min) - 1)
        number -= 1
    return output



# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    sorted_array = [0] * arr.length()
    for number in range(arr.length()):
        sorted_array[number] = arr[number] * arr[number]

    static_array = StaticArray(arr.length())
    for number, value in enumerate(sorted(sorted_array)):
        static_array[number] = value
    return static_array


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
