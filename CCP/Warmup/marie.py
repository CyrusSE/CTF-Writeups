def solve(N, X, A):
    if X == 0:
        return "Tidak Mustahil! owo"
    used = set()
    curr = 0
    for num in A:
        if num == X:
            return "Tidak Mustahil! owo"
    for i in range(N):
        if curr == X:
            return "Tidak Mustahil! owo"
        if (A[i] | X) != X:
            continue
            
        new = curr | A[i]
        if new & X > curr & X:
            curr = new
            used.add(i)
        if curr == X:
            return "Tidak Mustahil! owo"
    if curr == X:
        return "Tidak Mustahil! owo"
    return "Mustahil! o_o"

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    result = solve(N, X, A)
    print(result)

if __name__ == "__main__":
    main()