def solve(mat):
    # CODE HERE
    mat = dict(mat)
    list1 = sorted(set(mat.values()))
    a = list1[1]
    keys = [k for k, v in mat.items() if v == a]
    keys = sorted(keys)
    ' '.join(str(e) for e in keys)
    return keys
