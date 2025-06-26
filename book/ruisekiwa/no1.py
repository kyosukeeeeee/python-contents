N = int(input())

station = []
for _ in range(N):
    station.append(int(input()))

prefix = [0] * (N + 1)
for i in range(N):
    prefix[i + 1] = prefix[i] + station[i]

l, r = map(int, input().split())

result = prefix[r] - prefix[l]
print(result)