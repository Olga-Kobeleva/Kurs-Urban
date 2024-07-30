my_dict = {'Denis' : 1986, 'Olga' : 1987, 'Tat`yana' : 1963}
print(my_dict)
print(my_dict['Denis'])
my_dict['Artyom'] = 2000
print(my_dict)
my_dict.update({'Viktor' : 2003,
                'Andrey' : 1989})
a = my_dict.pop('Olga')
print(a)
print(my_dict)


my_set = {1, 2 ,2, 'Apple', 'Apple', 3.54}
print(my_set)
my_set.update([13, 77])
my_set.remove(2)
print(my_set)