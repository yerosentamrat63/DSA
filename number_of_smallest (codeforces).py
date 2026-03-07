n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
res = []
count = 0
idx = 0
jdx = 0
while jdx < m:
    while idx < n and arr1[idx] < arr2[jdx]:
        count += 1
        idx += 1
    
    res.append(count)
    jdx += 1
print(*res)
