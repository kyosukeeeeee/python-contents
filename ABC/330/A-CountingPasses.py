# 1行目: 人数と合格点
N, L = map(int, input().split())

# 2行目: N個の点数をまとめて取得
scores = list(map(int, input().split()))

# 合格者数カウント
total = 0
for score in scores:
    if score >= L:
        total += 1

print(total)