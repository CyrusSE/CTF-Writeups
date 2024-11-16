def calc(P, K):
    total = P
    t = 1
    while True:
        move = P // (K ** t)
        if move == 0:
            break
        total += move
        t += 1
    return total

def solve(N, Q):
    nama = []
    for _ in range(N):
        nama.append(input())
    cr = 0
    for _ in range(Q):
        P, K = map(int, input().split())
        total_jln = calc(P, K)
        cr = (cr + total_jln) % N
        print(nama[cr])

N, Q = map(int, input().split())

solve(N, Q)