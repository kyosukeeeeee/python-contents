N, T = map(int, input().split())

L = list(int().input().sprlit())
R = list(int().input().sprlit())

prefix = [0] * N
for i in range(N):
    for j in range(L[i], R[i]):
        prefix[j] += 1

print(prefix[X])