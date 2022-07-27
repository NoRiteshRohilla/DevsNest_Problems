def solve(n, arr, key):
    if key in arr:
        return arr.index(key)
    else:
        for i in range(len(arr)):
            if arr[i] > key:
                return i
    return len(arr)
