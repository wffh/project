# 1.chose different level to calculate (1.primary 2.middle)
# 2.make a mod 1:+ 2:- 3:* 4:/
# 3.input how many question you want to solve?
# 4.1.xxxx result is :    if right : yes else:try again

#! /usr/bin/env python3 
from random import randint

path = '/home/kali/project/math.txt'

def judge(result):
    global win
    try:
        answer = int(input())
    except ValueError:  
        print('Input can not None')
        exit()
    if result == answer:
        print('Good!You are right!')
        win += 1
    else:
        print('Error!')
        with open(path, 'a') as w:
            s = str(x) + a[oprt] + str(y) +  '=' + str(result) + '   '
            w.write(s)


def clt(i, cs):
    global a
    global x, y
    global oprt    
    a  = ['0','+','-','*','/']
    while(i):
        oprt = randint(1, cs) # oprt : make a mod 1:+ 2:- 3:* 4:/
        x = randint(0, 100)
        y = randint(0, 100) 
        if oprt == 1:
            print(x, a[oprt], y, '=', end=' ')
            result = x + y
            judge(result)
        elif oprt == 2:
            print(x, '-', y, '=', end=' ')
            result = x - y
            judge(result)
        elif oprt == 3:
            x = randint(0, 20)
            y = randint(0, 20) 
            print(x, '*', y, '=', end=' ')
            result = x * y
            judge(result)
        elif oprt == 4:
            print(x, '/', y, '=', end=' ')
            result = x // y
            judge(result)
        i -= 1
win = 0
print('-*-'*10)
print(' '*8 + '1.primary')
print(' '*8 + '2.middle')
print('-*-'*10)
try:
    cs = int(input('Please input the level you want to calculate: '))
    i = int(input('How many questions you want to solve: '))
except ValueError:
    print('Your level or the number of questions is wrong!!!')
    exit()
if cs == 1:
    clt(i, cs+1)
elif cs == 2:
    clt(i, cs+2)
else:
    print('Level is error')
    exit()
print('There are {} questions, your currect answer {}, wrong answer {}.\nAccuracy rate: {:.2f}%'.format(i, win, i-win, win/i*100))
