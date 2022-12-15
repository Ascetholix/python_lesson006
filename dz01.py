# Игра тетрис через тк интер
# с помошью lambda фнкции
import tkinter as tk

def user(a):   # главная функция
  global mot
  if mot%2==0:
    count_x(a)
    check(count_x(a))
    mot+=1
  else:
    count_o(a)
    check(count_o(a))
    mot+=1
      
def check(x):      # логика игры
  mas = ((btn1['text'] , btn2['text'] , btn3['text']),  # массив
         (btn4['text'] , btn5['text'] , btn6['text']),
         (btn7['text'] , btn8['text'] , btn9['text']))
  for col in range(3):              # цикл проверки по стобам
    if mas[0][col] == x and mas[1][col] == x and mas[2][col] == x:
      lbl['text'] = f'Победил {x}'
    if x =='x':
      lbl['bg'] = 'red'
    else:
      lbl['bg'] = 'blue'
      
  for row in range(3):         #цикл проверки по строкам
    if mas[row][0] == x and mas[row][1] == x and mas[row][2] == x:
      lbl['text'] = f'Победил {x}'
    if x =='x':
      lbl['bg'] = 'red'
    else:
      lbl['bg'] = 'blue'
      
  if mas[0][0] == x and mas[1][1] == x and mas[2][2] == x: # свреху вних с лева на право
    lbl['text'] = f'Победил {x}'
    if x =='x':
      lbl['bg'] = 'red'
    else:
      lbl['bg'] = 'blue'
      
  if mas[0][2] == x and mas[1][1] == x and mas[2][0] == x: # свреху вних с прова на лево
    lbl['text'] = f'Победил {x}'
    if x =='x':
      lbl['bg'] = 'red'
    else:
      lbl['bg'] = 'blue'
      
  
def res():          # рестарт
  btn1['state']=tk.NORMAL
  btn2['state']=tk.NORMAL
  btn3['state']=tk.NORMAL
  btn4['state']=tk.NORMAL
  btn5['state']=tk.NORMAL
  btn6['state']=tk.NORMAL
  btn7['state']=tk.NORMAL
  btn8['state']=tk.NORMAL
  btn9['state']=tk.NORMAL
  btn1['bg'] = 'white'
  btn2['bg'] = 'white'
  btn3['bg'] = 'white'
  btn4['bg'] = 'white'
  btn5['bg'] = 'white'
  btn6['bg'] = 'white'
  btn7['bg'] = 'white'
  btn8['bg'] = 'white'
  btn9['bg'] = 'white'
  btn1['text'] = ''
  btn2['text'] = ''
  btn3['text'] = ''
  btn4['text'] = ''
  btn5['text'] = ''
  btn6['text'] = ''
  btn7['text'] = ''
  btn8['text'] = ''
  btn9['text'] = ''
  lbl['text'] = ''

def count_x(a):
  if a ==1:
    btn1['text'] = 'x'
    btn1['bg'] = 'blue'
    btn1['state']=tk.DISABLED
  if a ==2:
    btn2['text'] = 'x'
    btn2['bg'] = 'blue'
    btn2['state']=tk.DISABLED
  if a ==3:
    btn3['text'] = 'x'
    btn3['bg'] = 'blue'
    btn3['state']=tk.DISABLED
  if a ==4:
    btn4['text'] = 'x'
    btn4['bg'] = 'blue'
    btn4['state']=tk.DISABLED
  if a ==5:
    btn5['text'] = 'x'
    btn5['bg'] = 'blue'
    btn5['state']=tk.DISABLED
  if a ==6:
    btn6['text'] = 'x'
    btn6['bg'] = 'blue'
    btn6['state']=tk.DISABLED
  if a ==7:
    btn7['text'] = 'x'
    btn7['bg'] = 'blue'
    btn7['state']=tk.DISABLED
  if a ==8:
    btn8['text'] = 'x'
    btn8['bg'] = 'blue'
    btn8['state']=tk.DISABLED
  if a ==9:
    btn9['text'] = 'x'
    btn9['bg'] = 'blue'
    btn9['state']=tk.DISABLED
  return 'x'
      
def count_o(a):
  if a ==1:
    btn1['text'] = 'o'
    btn1['bg'] = 'red'
    btn1['state']=tk.DISABLED
  if a ==2:
    btn2['text'] = 'o'
    btn2['bg'] = 'red'
    btn2['state']=tk.DISABLED
  if a ==3:
    btn3['text'] = 'o'
    btn3['bg'] = 'red'
    btn3['state']=tk.DISABLED
  if a ==4:
    btn4['text'] = 'o'
    btn4['bg'] = 'red'
    btn4['state']=tk.DISABLED
  if a ==5:
    btn5['text'] = 'o'
    btn5['bg'] = 'red'
    btn5['state']=tk.DISABLED
  if a ==6:
    btn6['text'] = 'o'
    btn6['bg'] = 'red'
    btn6['state']=tk.DISABLED
  if a ==7:
    btn7['text'] = 'o'
    btn7['bg'] = 'red'
    btn7['state']=tk.DISABLED
  if a ==8:
    btn8['text'] = 'o'
    btn8['bg'] = 'red'
    btn8['state']=tk.DISABLED
  if a ==9:
    btn9['text'] = 'o'
    btn9['bg'] = 'red'
    btn9['state']=tk.DISABLED
  return 'o'

mot = 0
win = tk.Tk() # начало
win.config(bg='black')  # Цвет фона окна в RGB или просто название на англиском  (rgb онлайн)
win.title('Крестики нолики')       #   Название окна
win.geometry("300x400+300+200")   #  Размер онка в пикселях и чурез + место вывода 
win.resizable(True, True)       # Изменение размера окна

lbl =tk.Label(win,font=('Arial', 20, 'bold'))

btn1 = tk.Button(win,command=lambda:user(1),font=('Arial', 20, 'bold'))
btn2 = tk.Button(win,command=lambda:user(2),font=('Arial', 20, 'bold'))
btn3 = tk.Button(win,command=lambda:user(3),font=('Arial', 20, 'bold'))
btn4 = tk.Button(win,command=lambda:user(4),font=('Arial', 20, 'bold'))
btn5 = tk.Button(win,command=lambda:user(5),font=('Arial', 20, 'bold'))
btn6 = tk.Button(win,command=lambda:user(6),font=('Arial', 20, 'bold'))
btn7 = tk.Button(win,command=lambda:user(7),font=('Arial', 20, 'bold'))
btn8 = tk.Button(win,command=lambda:user(8),font=('Arial', 20, 'bold'))
btn9 = tk.Button(win,command=lambda:user(9),font=('Arial', 20, 'bold'))
btn0 = tk.Button(win,text = 'Рестарт',command=res,font=('Arial', 10, 'bold'))

btn1.grid(row=0,column=0, stick='wnse',padx =2,pady=2)
btn2.grid(row=0,column=1, stick='wnse',padx =2,pady=2)
btn3.grid(row=0,column=2, stick='wnse',padx =2,pady=2)
btn4.grid(row=1,column=0, stick='wnse',padx =2,pady=2)
btn5.grid(row=1,column=1, stick='wnse',padx =2,pady=2)
btn6.grid(row=1,column=2, stick='wnse',padx =2,pady=2)
btn7.grid(row=2,column=0, stick='wnse',padx =2,pady=2)
btn8.grid(row=2,column=1, stick='wnse',padx =2,pady=2)
btn9.grid(row=2,column=2, stick='wnse',padx =2,pady=2)
btn0.grid(row=3,column=2, stick='wnse',padx =2,pady=2)
lbl.grid(row=3,column=0, stick='wnse',columnspan=2)

win.grid_columnconfigure(0,minsize=100)
win.grid_columnconfigure(1,minsize=100)
win.grid_columnconfigure(2,minsize=100)

win.grid_rowconfigure(0,minsize=100)
win.grid_rowconfigure(1,minsize=100)
win.grid_rowconfigure(2,minsize=100)
win.grid_rowconfigure(3,minsize=100)



win.mainloop()    # конец