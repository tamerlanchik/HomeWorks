from random import randint

a=[randint(1, 10) for i in range(10)]

print(*a)

K=int(input('������� K: '))

temp=a[-K:] #���������� ��������� � ���������

for i in range(10-K-1, -1, -1): #������ � ����� ������ �� ������ �������
    a[i+K]=a[i]
    
a[:K]=temp[:] #��������� � ������ ����������� � ���������

print(*a)