from random import randint
def reverce(q):
    for i in range(len(q)//2):
        q[i], q[-1-i]=q[-1-i], q[i] #при отрицательном индексе отсчет элементов в массиве ведется с конца, тогда q[-1]-самый последний
    return q
a=[randint(0, 10) for i in range(10)]
print(*a)
c=len(a)//2
print(*(reverce(a[:c])+reverce(a[c:])))

'''
Пример:
    1 7 7 6 2 9 6 4 2 4
    
    2 6 7 7 1 4 2 4 6 9
'''
#Запустить код можно на http://ideone.com/ . Язык Python 3.