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


findMedianSortedArrays("self", [1,3], [2])