def solve(n, arr):
    nummap = {}
    for i in range(len(nums)):
        if nums[i] in nummap:
            return 1
        else:
            nummap[nums[i]] = i
    return 0

# using only loop
def solve(n, arr):

    # CODE HERE

    for i in range(n):

        if arr[i] in arr[i+1:n]:

            return 1

    return 0
