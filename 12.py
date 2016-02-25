from random import randint
a=[randint(0, 100) for i in range(20)]
fib=[1, 1]
New=[]
while fib[-1]<100:
    fib.append(fib[-1]+fib[-2])
print(*fib)
print(*a)
    
def search(item):
    l=0
    r=len(fib)
    while l<r-1:
        c=(l+r)//2
        if fib[c]>item:
            r=c
        else:
            l=c
    if fib[l]==item:
        New.append(item)
        
for i in a:
    search(i)
    
print(*New)
#Запустить код можно на http://ideone.com/ . Язык Python 3. Есть нюанс: нужные входные данные нужно ввести во входной поток до запуска программы.
