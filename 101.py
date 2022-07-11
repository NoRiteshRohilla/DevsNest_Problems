def fib(n):

    if(n == 0):
        return 0
    
    if(n == 1 or n == 2):
        return 1

    else:
        return(fib(n-1) + fib(n-2))

n = 5
print("Fibonacci series of 5 numbers is: ", end = " ")
for i in range(0, n):
    print(fib(i), end = " ")

    