def solve(A, B, X, K):
    dist = B - A
    if dist % X == 0:
        return "Ya"
    rem = dist % X
    fow = rem
    back = X - rem
    if min(fow, back) <= K:
        return "Ya"
    return "Tidak :("

def main():
    A, B, X, K = map(int, input().split())
    result = solve(A, B, X, K)
    print(result)

if __name__ == "__main__":
    main()