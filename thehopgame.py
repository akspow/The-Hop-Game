n=int(input())
p=list(map(int,input().split(',')))
def res(arr,n):
    max=0
    pos=-1
    dc=1
    a=p[pos+1]
    if(pos>=n-1):
        return max
    if(pos+2>n-1):
        max+=n
        return max
    if(pos+3>n-1):
        max+=h
    b=2*p[pos+2]
    c=3*p[pos+3]
    if(a>b and a>c):
        pos+=1
        max+=a
        res(arr[pos:],n)
    elif(b>c):
        pos+=2
        max+=b
        res(arr[pos+2:],n)
    else:
        if dc>0:
           max+=c
           dc=0
           res(arr[pos+3:],n)
print(res(p,n))
