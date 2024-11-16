def count(N: int, M: int, X: int) -> int:
    count = 0
    for i1 in range(N):
        for j1 in range(M):
            for di in range(-X, X + 1):
                i2 = i1 + di
                if i2 < 0 or i2 >= N:
                    continue
                rem = X - abs(di)
                if rem < 0:
                    continue
                j2_pos = j1 + rem
                if j2_pos < M:
                    count += 1
                j2_neg = j1 - rem
                if rem != 0 and j2_neg >= 0:
                    count += 1

    return count // 2

N, M, X = map(int, input().split())
print(count(N, M, X))