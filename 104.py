
# Selection Sort

def select(arr):
    n = len(arr)
    for iter_num in range(n):
        min_idx = iter_num
        for curr in range(iter_num+1, n):
            if arr[curr]<arr[min_idx]:
                min_idx = curr
        arr[min_idx], arr[iter_num] = arr[iter_num], arr[min_idx]

arr = [12, 14, 7, 6, 4, 1, 3]
select(arr)
print(arr)