from random import randint
a=[randint(0, 100) for i in range(100)]
fib=[1, 1]
New=[]
for i in range(100):
    fib.append(fib[-1]+fib[-2])
    if fib[-1]>100: break
print(fib)
print(a)
    
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
    
print(New)