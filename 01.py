# Напишите программу вычисления арифметическое выражения заданого строкой.
# Используя операции +, -, /, *. приоритет операций стандарный
# пример 
# 2+2 = 4
# 1+2*3=7
# 1-2*3=-5
# Добавьте возможность использование скобок, меняющих приоритет опеации
# (1+2)*3 = 9
# 1 *  2 /  3 +  4 -

txt ='1 - 2*3'
count = 0
lst = [i for i in txt] # Переводим текст в список
ls = []
tmp = ''

for i in lst:  
  
  if ' ' in lst: # если есть пробелы удаляем их через цикл
    for j in lst:
      if j ==' ':
        lst.remove(j)
        
  if i.isdigit():  # если текст цифра то добавлям в tmp
    tmp+=i
  else:           # иначе
    ls.append(int(tmp))   # сформирований temp  добавляем в список
    ls.append(i)          # и добавляем в спиок знак 
    tmp=''                # temp очишаем
else:         #   иначе цикла 
  ls.append(int(tmp))    # добавляем в список последний  temp

print(ls)
  
while ('*' in ls) or ('/' in ls):
  mult = -1
  div = - 1
  if '*' in ls:
    mult = ls.index('*')
  if '/' in ls:
    div = ls.index('/')
  if ((mult < div) and ( mult != -1) and ( div !=-1)) or (( mult != -1) and  (div ==-1)):
    res = ls[mult-1] * ls[mult+1]
    ls = ls[:mult-1]+[res]+ls[mult+2:]
  elif ((mult > div) and ( mult != -1) and ( div !=-1)) or (( div != -1) and  (mult ==-1)):
    res = ls[div-1] / ls[div+1]
    ls = ls[:div-1]+[res]+ls[div+2:]
    
while ('+' in ls) or ('-' in ls):
  add = -1
  sub = - 1
  if '+' in ls:
    add = ls.index('+')
  if '-' in ls:
    sub = ls.index('-')
  if ((add < sub) and ( add != -1) and ( sub !=-1)) or (( add != -1) and  (sub ==-1)):
    res = ls[add-1] + ls[add+1]
    ls = ls[:add-1]+[res]+ls[add+2:]
  elif ((add > sub) and ( add != -1) and ( sub !=-1)) or (( sub != -1) and  (add ==-1)):
    res = ls[sub-1] - ls[sub+1]
    ls = ls[:sub-1]+[res]+ls[sub+2:]

print(res)
print(ls)
  
  
    
  


# print(tmp)
# print(ls)
# # print(res)
# print(ls.index('*')) 
    
  
