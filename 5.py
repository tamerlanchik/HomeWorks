from random import randint
a=[randint(0, 4) for i in range(1000)]
X=int(input('Введите, что искать: '))
if X<0 or X>4: print('Таких элементов нет')
else:
    for i in range(len(a)):
        if X==a[i]: print(i, end=' ')