
# Bubble sort

def bubble(arr):
    n = len(arr)
    for iter_num in range(n):
        for cur in range(n-1-iter_num):
            if arr[cur]>arr[cur+1]:
                arr[cur], arr[cur+1] = arr[cur+1], arr[cur]
            
arr = [12, 14, 7, 6, 4, 1, 3]
bubble(arr)
print(arr)