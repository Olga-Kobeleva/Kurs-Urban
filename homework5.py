immutable_tupel = 1, 2, 3, 'abc', True
immutable_tupel_2 = (1, 2, 3, 'abc', True)
print(immutable_tupel)
print(immutable_tupel_2)

#immutable_tupel[1] = 7
#print(immutable_tupel) # immutable_tupel[1] = 7 - выдает такую ошибку - картеж не изменяемый тип данных


mutable_list = [1, 3, 4, 'orange', 'lemon']
mutable_list[0] = 7
print(mutable_list)
