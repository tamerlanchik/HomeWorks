from random import randint
a=[randint(0, 10) for i in range(11)] #��������� ������ �� 11 ��������� �����
print(*a)
for i in range(1, len(a), 2): #�������� ���� �� 1 �� len(a) �� ������� � ����� 2
    a[i], a[i-1]=a[i-1], a[i] #�������� �������� �������
print(*a)

'''
������:
    4 10 0 5 10 6 3 7 3 8 7
    
    10 4 5 0 6 10 7 3 8 3 7
'''
#��������� ��� ����� �� http://ideone.com/ . ���� Python 3.
