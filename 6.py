from random import randint
a=[randint(0, 10) for i in range(11)] #��������� ������ �� 11 ��������� �����
print(*a)
for i in range(1, len(a), 2): #�������� ���� �� 1 �� len(a) �� ������� � ����� 2
    a[i], a[i-1]=a[i-1], a[i] #�������� �������� �������
print(*a)
