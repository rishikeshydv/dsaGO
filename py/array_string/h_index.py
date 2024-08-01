def hindex(citations):
    dp = [0]*len(citations)
    for c in citations:
        if c > (len(citations)-1):
            dp[-1] += 1
        else:
            dp[c] += 1
    
    cumulation = 0
    for i in range(len(citations)-1,-1,-1):
        cumulation += dp[i]
        if citations[i] <= cumulation:
            return cumulation
    
print(hindex([1,3,1]))
