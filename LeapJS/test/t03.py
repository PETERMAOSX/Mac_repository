def rotate(nums:list,k:int):
    if(len(nums) <= 1):
        return 1
    for _ in range(k):
        lastValue = nums.pop()
        nums.insert(0,lastValue)

nums = [1,2,3,4,5,6,7]
rotate(nums,3)
print(nums)