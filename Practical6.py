# Matrix chain Multiplication using Dynamic Programming

'''
Time Complexity: O(n^3)
Space Complexity: O(n^2)
'''

INF = float('inf')

def matrix_chain(p, n):
    
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][i] = 0
        
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            dp[i][j] = INF
            
            for k in range(i, j):
                q = (
                    dp[i][k] 
                    + dp[k + 1][j] 
                    + p[i - 1] * p[k] * p[j]
                )
                
                if q < dp[i][j]:
                    dp[i][j] = q
                    
            
    return dp[1][n]

def main():
    n = int(input("Enter the number of matrices: "))
    
    p = list(map(int, input(f"Enter {n + 1} dimensions:\n").split()))
        
    print("\nMinimum Multiplication =", matrix_chain(p, n))
    
if __name__ == "__main__":
    main()
    