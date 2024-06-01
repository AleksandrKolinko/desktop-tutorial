first = 34
second = 34
third = 34
if first == second and second == third:
    print(3)

first = 46
second = 84
third = 46
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)

first = 32
second = 31
third = 33
if first == second:
    print(3)
elif first == third:
    print(3)
elif second == third:
    print(3)
else:
    print(0)

            # Предоставил два решения, одно с использованием операторов and и or, второе без их использования.

    first = 34
    second = 34
    third = 34
    if first == (first + second + third) / 3:
        print(3)
    else:
        print('Числа не являются равными')

    first_1 = 46
    second_1 = 84
    third_1 = 46
    sum_ = first_1 + second_1 + third_1
    if first_1 == sum_ / 3:
        print(3)
    sum_2 = first_1 + second_1
    if first_1 == sum_2 / 2:
        print(2)
    sum_3 = first_1 + third_1
    if first_1 == sum_3 / 2:
        print(2)
    else:
        print(0)

    first_2 = 32
    second_2 = 31
    third_2 = 33
    if first_2 == second_2:
        print(3)
    elif first_2 == third_2:
        print(3)
    elif second_2 == third_2:
        print(3)
    else:
        print(0)
