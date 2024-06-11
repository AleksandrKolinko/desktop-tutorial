def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25, c=[1,2,3])
vaules_list = [5, 'Home', False]
vaules_dict = {'a': 32, 'b': 'Слово', 'c': True}
print_params(*vaules_list)
print_params(**vaules_dict)
vaules_list_2 = [54.32, "'Строка'"]
print_params(*vaules_list_2, 42)

