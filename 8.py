from random import randint
a=[randint(1, 10) for i in range(10)]
print(*a)
print('Введите K и M. Помните, нумерация элементов ведется с нуля.')
K, M=int(input('K: ')), int(input('M: '))
for i in range((M-K+1)//2):
    a[K+i], a[M-i]=a[M-i], a[K+i]
print(*a)
#Запустить код можно на http://ideone.com/ . Язык Python 3. Есть нюанс: нужные входные данные нужно ввести во входной поток до запуска программы.
