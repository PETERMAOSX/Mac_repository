def isAnagram(s: str, t: str) -> bool:
    count_a = 0
    count_b = 0
    for i in s:
        count_a += ord(i)
    for j in t:
        count_b += ord(j)
    if count_a == count_b:
        return True
    else:
        return False
print(isAnagram('ac','bb'))