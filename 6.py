from random import randint
a=[randint(0, 10) for i in range(11)] #создается массив из 11 рандомных чисел
print(*a)
for i in range(1, len(a), 2): #проходит цикл от 1 до len(a) не включая с шагом 2
    a[i], a[i-1]=a[i-1], a[i] #элементы меняются местами
print(*a)

'''
Пример:
    4 10 0 5 10 6 3 7 3 8 7
    
    10 4 5 0 6 10 7 3 8 3 7
'''
#Запустить код можно на http://ideone.com/ . Язык Python 3.
