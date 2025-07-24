#https://leetcode.com/problems/two-sum/description/

# def twoSum(list_, target):
#     num2 = 0
#     indexList = []
#     for i in list_:
#         num1 = i
#         print(num1, num2)
#         if (num1 + num2) == target:
#             print(num1, num2)
#             ind1 = list_.index(num1)
#             if num1 == num2:
#                 ind2 = list_.index(num2, ind1+1)
#             else:
#                 ind2 = list_.index(num2)
#             indexList = sorted([ind1, ind2])
#         else:
#             num2 = num1
#     print(indexList)

# twoSum([3,2,3], 6)

# def twoSum(nums, target):
#     list1 = []
#     for i in range(len(nums)):
#         #print(i, nums[i])
#         for j in range(1, len(nums)):
#             print(i, j, nums[i], nums[j], nums[i]+nums[j])
#             if nums[i]+nums[j] == target and i != j:
#                 list1 = [i,j]
#                 #return list1
#                 print(list1)
#                 print("*************")
import big_o
def twoSum(nums, target):
    diff = {}
    # key is the number in list and value is the index of list
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference not in diff:
            diff[nums[i]] = i
            print(diff)
        else:
            print(diff[difference], i)
            #return [diff[difference], i]

twoSum([3, 2, 3], 6)


# dictionary with enumerate

def twosUmsDict(nums, target):
    sums = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in sums:
            return [sums.get(diff), i]
        sums[num] = i
        print(sums)
        return []
twoSum([3, 2, 3], 6)
