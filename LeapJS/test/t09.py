def findfirstOneChar(s:str):
    n = len(s)
    dict_map = {}
    for i in range(n):
        s_char = s[i]
        if(dict_map.get(s_char) == 0):
            dict_map.setdefault(s_char,0)
        else:
            dict_map.setdefault(s_char,int(dict_map.get(s_char))+1)
        
    print(dict_map)
    for i in range(n):
        if dict_map.get(s[i]) == 1:
            return i
print(findfirstOneChar("maoshaoxiong"))
