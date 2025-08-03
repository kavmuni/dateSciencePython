#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class remove_duplicate:
    def rem_duplicate(strs:list):
        unique_list = []
        rec_count = 1
        strs_len = len(strs)
        #print(strs_len)
        unique_list.append(strs[0])
        while rec_count <= strs_len - 1:
            #print(f"record count variable: {rec_count}")
            #print(f"string length variable: {strs_len}")
            #print(f"strs[rec_count]: {strs[rec_count]}")
            if strs[rec_count] not in unique_list:
                unique_list.append(strs[rec_count])
                #print(f"printing unique list inside the if clause: {unique_list}")
            rec_count += 1
            #print("****************")
        unique_list.extend((strs_len - len(unique_list)) * "_") # important
        print(unique_list)

solution = remove_duplicate
solution.rem_duplicate([0,1,1,2,2,3,4,5,5,6,6,6,6,7,8,8,8,8,9])

