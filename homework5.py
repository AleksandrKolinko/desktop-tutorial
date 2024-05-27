immutable_var = (1, 2, 'String', True)  # Элементы кортежа являются неизменной коллекцией
print(immutable_var)

mutable_list = [1, 2, 'String', False]
print(mutable_list)
mutable_list.remove(2)
print(mutable_list)
mutable_list[1] = 5
print(mutable_list)
mutable_list.append('String')
print(mutable_list)