my_dict = {'Александр': 1995}
print(my_dict)
print(my_dict.get('Dima'))
my_dict['Aleksandr'] = 1996
print(my_dict)
my_dict.update({'Alexey': 2001,
               'Slava': 1998})
print(my_dict)
del my_dict['Александр']
print(my_dict)

my_set = {1, 2, 4, 7, 2, 1, 5, 2, 2, 1, 'String', True}
print(my_set)
my_set.add(8)
my_set.add(6)
my_set.discard('String')
print(my_set)
