
# dp[i][j] is going to store True if sum_a j is 
# possible with array elements from 0 to i. 

dp = []

# A recursive function to print all subsets with the help of dp[][]. Vector p[] stores current subset. 

def printSubsetsRec(arr, i, sum_a, p):
    global dp
    # If we reached end and sum_a is non-zero. We print p[] only if arr[0] is equal to sum_a OR dp[0][sum_a] is True. 
    if (i == 0 and sum_a != 0 and dp[0][sum_a]):
        p.append(arr[i])
        print(p)
        return
  
    # If sum_a becomes 0 
    if (i == 0 and sum_a == 0):
        print(p)
        return
  
    #If given sum_a can be achieved after ignoring current element. 
    if (dp[i-1][sum_a]):
        # Create a new vector to store path 
        b = p[:]
        printSubsetsRec(arr, i-1, sum_a, b)
  
    # If given sum_a can be achieved after considering current element. 
    if (sum_a >= arr[i] and dp[i-1][sum_a-arr[i]]):
        p.append(arr[i])
        printSubsetsRec(arr, i-1, sum_a-arr[i], p)

  
# Prints all subsets of arr[0..n-1] with sum_a 0. 
def printAllSubsets(arr, n , sum_a):
    global dp
    if (n == 0 or sum_a < 0):
       return
  
    # sum_a 0 can always be achieved with 0 elements 
    dp = [False] * n
    for i in range(n):
        #dp[i] = new bool[sum_a + 1]; 
        dp[i] = [False] * (sum_a + 1)
        dp[i][0] = True
      
    # sum_a arr[0] can be achieved with single element 
    if (arr[0] <= sum_a):
       dp[0][arr[0]] = True
  
    # Fill rest of the entries in dp[][] 
    for i in range(n):
        for j in range(sum_a+1):
            dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i]] if (arr[i] <= j) else dp[i-1][j]

    if (dp[n-1][sum_a] == False):
        print("There are no subsets with sum_a {}".format(sum_a))
        return
  
    # Now recursively traverse dp[][] to find all paths from dp[n-1][sum_a] 
    p = [] 
    printSubsetsRec(arr, n-1, sum_a, p)
  
# Driver code 

if __name__ == '__main__':
    arr = [i for i in range(1,27)]
    n = len(arr)
    sum_a = 53
    printAllSubsets(arr, n, sum_a)