# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.
# ['sdf13', 'fds66', '34']
# -> 3
# 'sdf13', '34'

enterList =list(map(str, input('Введите тексты: ').split()))

n = input('Число: ')

result = list(filter(lambda x: n in x, enterList))
print(result)
