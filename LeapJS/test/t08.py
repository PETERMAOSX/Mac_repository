def reverseNumber(x:int) -> int:
    ans = 0
    while x != 0:
        ans = ans * 10 + ans / 10
        x = x / 10
    return ans
print(reverseNumber(123))