def solve(n, nums, target):
    mid = (n-1)//2
    if n==0:
        return -1
    if target < nums[mid]:
        return solve(mid,nums[:mid],target)
    elif target > nums[mid]:
        sol = solve(n-mid-1,nums[mid+1:],target)
        return mid + 1 + sol if sol!=-1 else -1
    return mid
