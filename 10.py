from random import randint
a=[randint(1, 200) for i in range(10)]
print(*a)
n=int(input('������� N: '))
New=[]
for i in a:
    ans=0
    temp=i
    for k in range(3): #���������� ����� ����
        ans+=temp%10
        temp//=10   
    if ans==n:
        New.append(i)   #��������� ����� � ����� �������, ��� �� �������
if len(New)!=0: print(*New)
else: print('������ �� ������� :( ')
#��������� ��� ����� �� http://ideone.com/ . ���� Python 3. ���� �����: ������ ������� ������ ����� ������ �� ������� ����� �� ������� ���������.
