def bs(arr, x):
    l, r = 0, len(arr)-1
    while l<=r:
        m = (l+r)//2
        if arr[m]==x:
            return m
        if arr[m]>x:
            r = m - 1
        else:
            l = m+1
        return -1

arr = [2,4,5,16,32,37,54,68,82,119]