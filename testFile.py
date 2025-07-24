strs = ["flower", "flow", "flowers", "flo", "fl", "cars"]


def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""

    pre_dic = {}
    for i in strs:
        for j in range(1, len(i) + 1):
            sliced = i[:j]
            #print(sliced)
            pre_dic[sliced] = pre_dic.get(sliced, 0) + 1
            #print(pre_dic)

    max_len = 0
    key_l = []
    print(pre_dic)
    for key, value in pre_dic.items():
        if value == len(strs) and len(key) > max_len:
            print(value, len(strs), len(key), max_len)
            key_l = [key]
            max_len = len(key)
    print(key_l)
    if key_l:
        print(key_l)
        return max(key_l)
    else:
        if len(strs) == 1:
            return strs[0]
        return ""

longestCommonPrefix(strs)