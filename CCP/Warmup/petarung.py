from heapq import heapify, heappush, heappop

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
fighters = list(map(int, input().split()))
heapify(fighters)  

while len(fighters) > 1:
    a = heappop(fighters) 
    b = heappop(fighters)  
    g = gcd(a, b)
    winner = (a + b) // g
    heappush(fighters, winner)  

print(fighters[0])