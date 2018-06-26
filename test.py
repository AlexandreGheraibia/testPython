x="Hello word!"
print(x)

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(10))


def isPrime(n):
    i=2
    while i<n and n%i!=0:
        i=i+1

    return i==n



def PrimeNum(l):
    i=0
    l2=[]
    while i<len(l):
        if(isPrime(l[i])):
            l2.append(l[i])
        i=i+1
    return  l2


def somme(l):
    i=0
    res=0
    while i<len(l):
        res+=l[i]
        i=i+1
    return  res

def min(l):
    i=0
    valMin=l[i]
    while i<len(l):
        if(valMin>l[i]):
            valMin=l[i];
        i=i+1
    return  valMin

def max(l):
    i=0
    valMax=l[i]
    while i<len(l):
        if(valMax<l[i]):
            valMax=l[i];
        i=i+1
    return  valMax
def reverse(l):
    n=len(l)
    i=n-1
    valMax=l[i]

    while i>=0:
        tmp=l[i]
        l.remove(tmp)
        l.append(tmp)
        i=i-1
    return l

l=[11,21,31,41,51]
l.append(9)#concat/add
l.remove(9)
#l=range(1,10)
res=PrimeNum(l)
print(res)
for i in res:
    print(i)
print(somme(l))
print(res)
print(min(l))
print(max(l))
l=['A','L','E','X']
print(l)
print(reverse(l))