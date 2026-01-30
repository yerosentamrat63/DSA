import sys

res = {}
n = int(input())

for i in range(n):
    name, phone_n = input().split(" ")
    res[name] = phone_n


for line in sys.stdin:
    query = line.strip()
    if query in res:
        print(f"{query}={res[query]}")
    else:
        print("Not found")
