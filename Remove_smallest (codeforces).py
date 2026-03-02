t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    idx = 0
    while len(a) > 1:
        if abs(a[idx] - a[idx + 1]) == 1:
            smallest = min(a[idx], a[idx + 1])
            a.remove(smallest)
        elif abs(a[idx] - a[idx + 1]) == 0:
            a.remove(a[idx])
        else:
            print("NO")
            break
    if len(a) == 1:
        print("YES")
