def count(y,x,n):
    return ((y-x)*(n-2))+1
n,x,y=map(int,input().split())
out=count(y,x,n)
print(out)
