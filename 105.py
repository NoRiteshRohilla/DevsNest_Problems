
# Insertion sort

def insertion(arr):
    n = len(arr)
    for wall in range(1, n):
        curr = arr[wall]
        pos_ptr = wall-1
        while pos_ptr+1>=0 and curr<arr[pos_ptr]:
            arr[pos_ptr+1] = arr[pos_ptr]
            pos_ptr-=1
            arr[pos_ptr+1] = curr
            
arr = [12,14,7,6,4,1,3]
insertion(arr)
print(arr)