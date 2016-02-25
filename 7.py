from random import randint
def reverce(q):
    for i in range(len(q)//2):
        q[i], q[-1-i]=q[-1-i], q[i] #ïðè îòðèöàòåëüíîì èíäåêñå îòñ÷åò ýëåìåíòîâ â ìàññèâå âåäåòñß ñ êîíöà, òîãäà q[-1]-ñàìûé ïîñëåäíèé
    return q
a=[randint(0, 10) for i in range(10)]
print(*a)
c=len(a)//2
print(*(reverce(a[:c])+reverce(a[c:])))

'''
ðèìåð:
    1 7 7 6 2 9 6 4 2 4
    
    2 6 7 7 1 4 2 4 6 9
'''
#Запустить код можно на http://ideone.com/ . Язык Python 3. Есть нюанс: нужные входные данные нужно ввести во входной поток до запуска программы.
