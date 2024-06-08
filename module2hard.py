for index in range(3, 21):
    list_ = []
    for i in range(1, index):
        for j in range(i + 1, index):
            if index % (i + j) == 0:
                list_.append(f'{i}{j}')
    print(index, ''.join(list_))
