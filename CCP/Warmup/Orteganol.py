def check_orteganol(freq):
    freqs = [f for f in freq.values() if f > 0]
    return len(freqs) > 0 and len(set(freqs)) == 1

def solve(N, A, B, S):
    count = 0
    for len_window in range(A, B + 1):
        freq = {}
        for i in range(len_window):
            freq[S[i]] = freq.get(S[i], 0) + 1
        if check_orteganol(freq):
            count += 1
        for i in range(len_window, N):
            freq[S[i - len_window]] -= 1
            freq[S[i]] = freq.get(S[i], 0) + 1
            if check_orteganol(freq):
                count += 1
                
    return count

def main():
    N, A, B = map(int, input().split())
    S = input().strip()

    result = solve(N, A, B, S)
    print(result)

if __name__ == "__main__":
    main()