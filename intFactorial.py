def fac(n):
    if (n == 0 or n == 1):
        return 1
    # if (n >1):
    else:
        # return (fac(n*fac(n-1)))
        return n * fac(n-1)

if __name__ =='__main__':
    n = int(input())
    print('factorial of n', n, "is:",fac(n))
