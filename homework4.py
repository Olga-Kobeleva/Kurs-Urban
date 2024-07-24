name = input('Введите ваше ФИО: ')   #input - произвольный текст
num = int(input("Сколько вам лет? "))
str_num = str(num)   #преобразование в строку
length = len(str_num)  #len - кол-во символов в введеном тексте
print('Здравствуйте,', name)
print(length)

print(name.upper())
print(name.lower())
print(name.replace(' ', ''))
print(name [0])
print(name [-1])


