def fibo(n: int) -> int:
    """ General concept with recursion """
    if n == 0:
        return 1
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)

def top_down_fibo(n: int) -> int:
    """ Recursive + Memorize(dict, cache) """
    memo = dict()
    return top_down_helper(n, memo)

def top_down_helper(n, memo):
    """his function help to export memo in sense of recursion """
    if n == 0:
        memo[n] = 0
    if n <= 2:
        memo[n] = 1    
    if n not in memo.keys():
        memo[n] = top_down_helper(n-1, memo) + top_down_helper(n-2, memo)
    return memo[n]

def bottom_up_fibo_forward(n):
    """
    Forward: (Known) several subproblem *calculate* other subproblem

    f(i-1) -----
                |
                |--calculate--> f(i)
                |
    f(i-2) -----

    """
    dp = []
    dp.append(0)
    dp.append(1)

    for i in range(1, n):
        dp.append(dp[i] + dp[i-1])
    return dp[n]

def bottom_up_fibo_backward(n):
    """
    Backward: (Known) one subproblem can *contribute* other subproblem 

      ------> contribute f(i+1)
      |
    f(i) 
      |
      ------> contribute f(i+2)

    """
    dp = [0] * (n+2)
    dp[0] = 0
    dp[1] = 1

    for i in range(1, n):
        dp[i+1] += dp[i]
        dp[i+2] += dp[i]
        # print(dp) # print this line to see how it work
    return dp[n]

print(bottom_up_fibo_forward(10) == bottom_up_fibo_backward(10))
print(bottom_up_fibo_backward(10) == top_down_fibo(10) == fibo(10))
