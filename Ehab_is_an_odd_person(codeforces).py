n = int(input())
arr = list(map(int, input().split()))
 
even = False
for elem in arr:
    if elem % 2 == 0:
        even = True
        break
 
odd = False
for num in arr:
    if num % 2 != 0:
        odd = True
        break
if even and odd:
    arr.sort()
print(*arr) 
