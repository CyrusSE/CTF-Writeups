def solve(N, M, K):
    MOD = 10**9 + 7
    dp = {}
    
    def count_ways(pos, jumps_left):
        if jumps_left == 0:
            return 1 if pos == N else 0
        if pos == N:
            return 0  
        state = (pos, jumps_left)
        if state in dp:
            return dp[state]
        ways = 0
        for jump in range(1, M + 1):
            next_pos = pos + jump
            if next_pos > N:
                bounce_back = N - (next_pos - N)
                if bounce_back >= 0:  
                    ways = (ways + count_ways(bounce_back, jumps_left - 1)) % MOD
            else:
                ways = (ways + count_ways(next_pos, jumps_left - 1)) % MOD
        
        dp[state] = ways
        return ways

    total = 0
    for jumps in range(1, K + 1):
        total = (total + count_ways(0, jumps)) % MOD
    
    return total

def main():
    N, M, K = map(int, input().split())
    result = solve(N, M, K)
    print(result)

if __name__ == "__main__":
    main()