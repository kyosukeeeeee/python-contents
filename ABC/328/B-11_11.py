N = int(input())
D = list(map(int, input().split()))

total = 0

for month in range(N):
    if(len(set(str(month + 1))) == 1):
        for day in range(D[month]):
            if(len(set(str(month + 1) + str(day + 1))) == 1):
                total += 1

print(total)