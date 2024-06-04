my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
initial_index = 0
while initial_index < len(my_list):
    if my_list[initial_index] < 0:
        break
    if my_list[initial_index] > 0:
        print(my_list[initial_index])
    initial_index = initial_index + 1