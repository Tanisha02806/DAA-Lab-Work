# Knapsack using Dynamic Programming

'''
Time Complexity: O(n * W)
Space Complexity: O(n * W)

where, n = number of items and W = Maximum capacity of knapsack
'''

from itertools import product

def knapsack(wt, val, n, W):
    
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i, w in product(range(1, n + 1), range(1, W + 1)):
        dp[i][w] = max(
            val[i - 1] + dp[i - 1][w - wt[i - 1]],
            dp[i - 1][w]
        ) if wt[i - 1] <= w else dp[i - 1][w]

    return dp[n][W]


def main():
    n = int(input("Enter number of items: "))
    
    wt = list(map(int, input("Enter weights: ").split()))
    val = list(map(int, input("Enter values: ").split()))
    
    W = int(input("Enter knapsack capacity: "))

    print("\nMaximum Profit =", knapsack(wt, val, n, W))
    
if __name__ == "__main__":
    main()



    
