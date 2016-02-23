from random import randint

a=[randint(1, 10) for i in range(10)]

print(*a)

K=int(input('Введите K: '))

temp=a[-K:] #запоминаем последние К элементов

for i in range(10-K-1, -1, -1): #проход с конца отреза до начала массива
    a[i+K]=a[i]
    
a[:K]=temp[:] #вставляем в начало запомненные К элементов

print(*a)