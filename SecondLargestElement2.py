def solve(n, arr):
    # CODE HERE
    max= 0
    for i in range(n):
        if(arr[i]>max):
            max=arr[i]
    arr.remove(max)
    max1= 0
    for i in range(n-1):
        if(arr[i]>max1 and arr[i]!=max):
            max1=arr[i]
    return max1
