N, Q = map(int, input().split())
S = input()

same = [0] * (N - 1)
for i in range(N - 1):
    if S[i] == S[i + 1]:
        same[i] = 1

prefix = [0] * N
for i in range(1, N):
    prefix[i] = prefix[i - 1] + same[i - 1]

for _ in range(Q):
    l, r = map(int, input().split())
    print(prefix[r - 1] - prefix[l - 1])