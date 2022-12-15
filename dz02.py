# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# с использованием map
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def func(list: list):
  maxi = 0
  mini = list[0]
  for i in list:
    while i > 1:
      i-=1
    if i != 1:
      if i < mini:
        mini = i
      elif i > maxi:
        maxi = i
  return round(maxi-mini,2)

floatList = list(map(float, input('Введите вещественые число через пробел: ').split()))

        
print(func(floatList))