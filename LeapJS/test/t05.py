def intersection(nums1:list,nums2:list) -> list:
    dict_map = {}
    for i in nums1:
        count = 0
        if(dict_map.get(i)) == 0:
            count = 1
        else:
            count += 1
        dict_map[i] = count
    insection = []
    for j in nums2:
        count = dict_map.get(i)
        if(count > 0):
            insection.append(i)
            count -= 1
            if count > 0:
                dict_map[i] = count
            else:
                dict_map[i] = None
    return insection
num1 = [1,2,3,3,4,5,6]
num2 = [1,2,3,5]
print(intersection(num1,num2))

