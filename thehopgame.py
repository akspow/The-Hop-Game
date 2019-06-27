n=int(input())
p=list(map(int,input().split(',')))
def res(p,n,pos):
    array=[0,0,0]
    dc=1
    mx=0
    for i in range(n):
        if(pos>=n-1):
            return mx
        if(pos+1>=n-1):
            mx+=p[pos+1]
            return mx
        if(pos+2>=n-1):
            mx+=max(p[pos+1]+p[pos+2],2*p[pos+2])
            return mx
        array[2]=p[pos+3]*3
        array[1]=p[pos+2]*2+p[pos+3]
        array[0]=max(p[pos+1]+p[pos+2]+p[pos+3],p[pos+1]+2*p[pos+3])
        if(max(array)==array[2]):
            if(dc>0):
                    pos+=3
                    dc=0
                    mx+=array[2]
                    res(p,n,pos)
            else:
                array[2]=0
        if(max(array)==array[1]):
            pos+=3
            mx+=array[1]
            res(p,n,pos)
        if(max(array)==array[0]):
            pos+=3
            mx+=array[0]
            res(p,n,pos)
maximum=res(p,n,-1)
print(maximum)
