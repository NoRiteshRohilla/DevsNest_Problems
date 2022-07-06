def solve(n, arr):
    # CODE HERE
    a = max(arr)
    while a in arr:
        arr.remove(a)
    return max(arr)
