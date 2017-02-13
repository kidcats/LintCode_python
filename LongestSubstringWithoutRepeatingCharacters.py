def longestStr(str):
    left = 0
    ans = 0
    last = {}
    for i in range(len(str)):
        if str[i] in last and last[str[i]] > left:
            left = last[str[i]] + 1
        last[str[i]] = i
        ans = max(ans,i-left+1)
    return ans

print(longestStr('ab++--lia'))