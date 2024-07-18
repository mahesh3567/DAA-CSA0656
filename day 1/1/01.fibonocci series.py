def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def fibseries(n):
    series=[]
    for i in range(n+1):
        series.append(fib(i))
    return series
print("B.MAHESH REDDY \n 192210708")
nth=int(input("enter a number:"))
print(fibseries(nth))
