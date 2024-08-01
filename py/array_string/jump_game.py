def jump(nums,n,ct):
    if ct >= n:
        return True

    if nums[ct] != 0:
        val = nums[ct]
        i = 1
        while i <= val:
            ct += i
            jump(nums[ct:],n,ct)
            i+=1
    else:
        jump(nums[ct:],n,ct+1)








num_list = [2,3,1,1,4]
print(jump(num_list,len(num_list),0))

