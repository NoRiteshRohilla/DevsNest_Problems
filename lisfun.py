def linear_search(li, ele):
    #li is the list and ele is the element to be search
    for i in range(len(li)):
        if li[i] == ele:
            return i
    return -i

li = [1,2,3,6,5]
index = linear_search(li, 6)
print(index)
