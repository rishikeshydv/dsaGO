def duplicate(nums):
    ct = 1
    for i in range(1,len(nums)-1):
        if nums[i] == nums[ct-1]:
            continue
        else:
            nums[ct] = nums[i]
            ct+=1
    return ct
print(duplicate([0,0,1,1,1,2,2,3,3,4]))
