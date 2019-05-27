def sum(n):
    x,y,count,s=1,2,0,0
    while count<n:
        s+=y/x
        x,y=y,x+y
        count+=1
    return float('{:.2f}'.format(s))
n=int(input())
sum(n)
