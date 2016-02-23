from random import randint
a=[randint(0, 100) for i in range(10)]
print(a)
def isPrime(n):
    if n<2: return False
    elif n>2 and n%2==0: return False
    else:
        t=3
        while t**2<n and n%t!=0:
            t+=2
        return t*t>n

New=[]
for i in a:
    if isPrime(i)==True:
        New.append(i)
if len(New)==0:
    print('Все составные')
else:
    print(*New)
    
#Запустить код можно на http://ideone.com/ . Язык Python 3. Есть нюанс: нужные входные данные нужно ввести во входной поток до запуска программы.
