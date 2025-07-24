# https://leetcode.com/problems/longest-common-prefix/description/
from pyarrow import nulls
# Best Solution

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#
#         prefix = strs[0]
#
#         for s in strs[1:]:
#             while not s.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if not prefix:
#                     return ""
#
#         return prefix


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # return -1 for empty list
        if len(strs) == 0:
            return -1
        elif strs[0] == "":
            return ""
        # find the shortest string in given list
        # {len(name):name for name in strs} ->
        # Since flight and flower are of length 6 latest is replacing the former and only {6: "flight", 4:"flow"} is printed
        # str_dict = {tuple(name): len(name) for name in strs}
        # print(str_dict)
        # str_dict = {len(name):name for name in strs}
        # print(str_dict)
        # small_string = [key for key, value in str_dict.items() if value == min(str_dict.values())]
        # print(small_string)
        # long_prefix = ""
        # rec = 0
        # for i in min(small_string):
        #     rec += 1
        #     print(i)
        #     #if i == str_dict[rec][i]:
        #     print(str_dict[rec])
        # str_dict = {i: (len(j),j) for i,j in enumerate(strs)} # forming a dictionary with its positing and (string, length) as tuple
        # print(str_dict)
        # small_string = min(str_dict.values())[1] # getting the minimum lenght string
        # strs_len = len(strs) # getting length of the list
        # #print(strs_len)
        # long_prefix = []
        # print(small_string)
        # rec = 0 # parameter is intialized to check length of the input list
        # for i in small_string: # iterating each character of the shortest word in given list
        #     rec += 1
        #     for j, k in enumerate(strs):
        #         for l in k:
        #             print(k, j,"<=", strs_len," ", j+1, "<=", len(k), " ", i, " == ", l)
        #             if j <= strs_len and j+1 <= len(k) and i not in long_prefix and j == rec:
        #                 if i == l:
        #                     print(i)
        #                     print(l)
        #                     long_prefix.append(l)
        #                 else:
        #                     break
        #             else:
        #                 continue
        # print("".join(long_prefix))3
        str_dict = {}
        for i in strs:
            for j in range(1,len(i)+1):
                str_slice = i[:j]
                str_dict[str_slice] = str_dict.get(str_slice, 0) + 1
        print(str_dict)
        max_occurrence = max(str_dict.values())
        prefix_list = [key for key, value in str_dict.items() if value == max_occurrence and value == len(strs)]
        print(prefix_list)
        if prefix_list:
            print(max(prefix_list))
        else:
            print("")




testString = Solution()
testString.longestCommonPrefix([""])