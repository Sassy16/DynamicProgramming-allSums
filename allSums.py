def allSumsDP(arr):
    res = set()
    res.add(0)
    for i in range(len(arr)):
        for j in res.copy():
            res.add(j+arr[i])
    return res