count = 0
matrix = []
for _ in range(5):
    matrix.append(list(map(int, input().split())))
idx = []
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            idx = [i, j]
print(abs(2-idx[0]) + abs(2-idx[1]))
