#https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/description/?envType=daily-question&envId=2025-07-18
from serial.tools.list_ports_common import numsplit


def minimumDifference(nums: list[int]) -> int:
    n = len(nums)
    num1 = 0
    num2 = 0
    nums1 = []
    if 1 == 1:
        for i in range(n):
            nums1 = nums
            print(nums1, i, nums)
            print(nums1[i])
            nums1.remove(nums1[i])
            print(nums1)
            num1 = sum(nums1)
            if num1 < num2:
                num2 = num1

    return num2

v = minimumDifference([1,3,2])
print(v)