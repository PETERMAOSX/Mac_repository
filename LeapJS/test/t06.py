def moveZero(nums:list):
    #直接删除为0的那一项，然后再在列表最后添加上0即可
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(0)
def moveZero01(nums:list):
    #先求出列表中含有的0的个数，然后再新开辟一个列表
    #把非0的项加入那个新开的列表
    #最后再加入0即可
    n = len(nums)
    zero_count = 0
    for i in nums:
        if i == 0:
            zero_count += 1
    ans = []
    for i in nums:
        if i != 0:
            ans.append(i)
    while (zero_count != 0):
        ans.append(0)
        zero_count -= 1
    for i in range(n):
        nums[i] = ans[i]
def movezero02(nums:list) -> None:
    lastNumberAt = 0
    for i in range(len(nums)):
        if(nums[i] != 0):
            nums[lastNumberAt] = nums[i]
            lastNumberAt = lastNumberAt + 1
    for i in range(lastNumberAt,len(nums)):
        nums[i] = 0

            
nums = [0,1,0,3,12]
movezero02(nums)
print(nums)