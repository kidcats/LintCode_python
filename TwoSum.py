def twoSum(head,target):
    hash={}
    for i in range(len(head)):
        if head[i] in hash:
            return [hash[head[i]],i+1]
        hash[target-head[i]]=i+1


if __name__=='__main__':
    l=[7,2,3,4]
    a=twoSum(l,9)
    print(a[0])