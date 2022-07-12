def fib(n):
    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        return 1
    else:
        return(fib(n-1)+fib(n-2))


n = int(input())
print("fibonacci series of asking number is: ", end=" ")
for i in range(0, n):
    print(fib(i), end=" ")
