# https://leetcode.com/problems/merge-two-sorted-lists/
#class merge_two_sorted_array:
# single-linked list. This has data as well as pointed to next location
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#
# def merge_2_sorted_array(nums1, nums2):
#     dummy = Node(-1)
#     curr = dummy
#     while nums1 is not None and nums2 is not None:
#         if nums1.data <= nums2.data:
#             print(nums1.data)
#             curr.next = nums1
#             nums1 = nums1.next
#         else:
#             print(nums2.data)
#             curr.next = nums2
#             nums2 = nums2.next
#         print(curr)
#         curr = curr.next
#
#     if nums1 is not None:
#         curr.next = nums1
#     elif nums2 is not None:
#         curr.next = nums2
#     print(curr)
#     return dummy.next
#
# def printList(head):
#     while head is not None:
#         print(head.data, end=" ")
#         head = head.next
#     #print()
#
# if __name__ == "__main__":
#     # First linked list: 5 -> 10 -> 15 -> 40
#     head1 = Node(5)
#     head1.next = Node(10)
#     head1.next.next = Node(15)
#     head1.next.next.next = Node(40)
#
#     # Second linked list: 2 -> 3 -> 20
#     head2 = Node(2)
#     head2.next = Node(3)
#     head2.next.next = Node(20)
#
#     res = merge_2_sorted_array(head1, head2)
#
#     printList(res)

def merge_2_sorted_list(nums1, nums2):
    sorted_array = []
    m  = len(nums1)
    n  = len(nums2)

    i = 0
    j = 0

    while i < m and j < n:
        print(f"i = {i} and m = {m} and j = {j} and n = {n}")
        if nums1[i] < nums2[j]:
            sorted_array.append(nums1[i])

            i += 1
        else:
            sorted_array.append(nums2[j])

            j += 1
    print(f"i = {i} and m = {m} and j = {j} and n = {n}")
    while i < m:
        sorted_array.append(nums1[i])
        i += 1

    while j < n:
        sorted_array.append(nums2[j])
        j += 1

    print(sorted_array)
    return sorted_array

merge_2_sorted_list([1,3,5,7], [2,4,6,8])

