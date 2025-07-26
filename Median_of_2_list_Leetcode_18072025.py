# https://leetcode.com/problems/median-of-two-sorted-arrays/
def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        fullList = sorted(nums1 + nums2)
        len_fullList = len(fullList)
        if len_fullList % 2 == 0:
            #print(len_fullList//2)
            lvMedian = (fullList[(len_fullList//2)-1] + fullList[len_fullList//2])/2
        else:
            lvMedian = fullList[(len_fullList-1)//2]
        print(lvMedian)

a = [1, 12, 15, 26, 38]
b = [2, 13, 17, 30, 45, 60]
findMedianSortedArrays("self", a, b)

## using Binary search method
# constraints: Array should be sorted
# def findMedianBinarySort(nums1):
#     #even though arrays are sorted individually when combined we should sort it again
#     """
#     Given 2 arrays are already sorted, so find median 2 arrays separate and find combined average
#     """
#     left = 0
#     right = len(nums1) - 1
#     while left <= right:
#         left += 1