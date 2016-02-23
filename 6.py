from random import randint
a=[randint(0, 10) for i in range(11)] #создаетс€ массив из 11 рандомных чисел
print(*a)
for i in range(1, len(a), 2): #проходит цикл от 1 до len(a) не включа€ с шагом 2
    a[i], a[i-1]=a[i-1], a[i] #элементы мен€ютс€ местами
print(*a)
