from random import randint
a=[randint(1, 10) for i in range(10)]
print(*a)
print('������� K � M. �������, ��������� ��������� ������� � ����.')
K, M=int(input('K: ')), int(input('M: '))
for i in range((M-K+1)//2):
    a[K+i], a[M-i]=a[M-i], a[K+i]
print(*a)
#��������� ��� ����� �� http://ideone.com/ . ���� Python 3. ���� �����: ������ ������� ������ ����� ������ �� ������� ����� �� ������� ���������.