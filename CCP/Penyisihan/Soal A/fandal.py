def solve(N, K, A, B):

    if K >= N:
        return 0, 0

    ba = K
    ca = 0
    while ba < N:
        ca += 1
        ba += A
    bb = K
    cb = 0
    while bb < N:
        cb += 1
        bb += B

    return cb, ca

N, K = map(int, input().split())
A, B = map(int, input().split())

min_r, max_r = solve(N, K, A, B)
print(min_r, max_r)