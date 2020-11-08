def twoSum(nums:list,target:int) -> list:
    dict_map = {}
    for i in range(len(nums)):
        if target-nums[i] in dict_map.keys():
            return [dict_map.get(target-nums[i]),i]
        dict_map[nums[i]] = i
    return []
nums = [3,2,4]
ans = twoSum(nums,7)
print(ans)