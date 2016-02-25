from random import randint
a=[randint(1, 200) for i in range(10)]
print(*a)
n=int(input('Ââåäèòå N: '))
New=[]
for i in a:
    ans=0
    temp=i
    for k in range(3): #âû÷èñëåíèå ñóììû öèôð
        ans+=temp%10
        temp//=10   
    if ans==n:
        New.append(i)   #äîáàâëÿåò ÷èñëî â êîíåö ìàññèâà, êàê ïî çàäàíèþ
if len(New)!=0: print(*New)
else: print('Íè÷åãî íå íàéäåíî :( ')
#Запустить код можно на http://ideone.com/ . Язык Python 3. Есть нюанс: нужные входные данные нужно ввести во входной поток до запуска программы.
