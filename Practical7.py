# Coin Change using Dynamic Programming

'''
Time Complexity: O(n * Amount)
Space Complexity: O(Amount)

where,
n = number of coin denominations
Amount = total amount to make
'''

INF = float('inf')

def coin_change(coins, n, amount):
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for j in range(n):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    
    return -1 if dp[amount] == INF else dp[amount]

def main():
    n = int(input("Enter the number of coin denominations: "))
    
    coins = list(map(int, input("Enter the coin denominations: ").split()))
    
    amount = int(input("Enter the amount: "))
    
    ans = coin_change(coins, n, amount)
    
    if ans == -1:
        print("\nChange cannot be made.")
    else:
        print("\nMinimum number of coins required=",ans)

if __name__ == "__main__":
    main()