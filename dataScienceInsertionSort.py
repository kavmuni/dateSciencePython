from insertionSort import insertionSort # package name and function name
# by default function returns void or NULL
"""
Insertion sort is to compare the elements with left element
"""
list1 = [3,6,4,1,4,7]
print(insertionSort(list1))
print(insertionSort(list("abfged")))

# Bubble sort
# for i in range(len(list1)):
#     #print("i:",i)
#     for j in range(i+1,len(list1)):
#         if list1[i] > list1[j]:
#             list1[i], list1[j] = list1[j], list1[i]
# print(list1)

# for i in range(1, len(list1)):
#     print(f"iteration {i}")
#     pos =list1[i]
#     print(f"pos: {pos}")
#     j = i - 1
#     print(f"j: {j}")
#     while j >= 0 and pos < list1[j]:
#         print("inside while loop")
#         print(f"list1: {list1}")
#         list1[j+1] = list1[j]
#         print(f"list1[j+1]: {list1[j+1]}")
#         print(f"list1[j]: {list1[j]}")
#         j = j-1
#         print(f"j: {j}")
#     list1[j+1] = pos
#     print(f"list1[j+1]: {list1[j+1]}")
#     print(f"pos: {pos}")
#     print(f"list1: {list1}")
#     print("****************")
# print(list1)
#arr = [10, 12, 30]
# for i in range(1,len(arr)):
#   pos = arr[i]
#   #print(f"print pos {pos}")
#   j = i-1 #1
#   #print(f"The value of j: {j}")
#   for j in arr[:i][::-1]:
#     #pos < arr[j]:
#     #arr[j+1] = arr[j]
#     #j = j-1






