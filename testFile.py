# strs = ["flower", "flow", "flowers", "flo", "fl", "cars"]
#
#
# def longestCommonPrefix(strs: list[str]) -> str:
#     if not strs:
#         return ""
#
#     pre_dic = {}
#     for i in strs:
#         for j in range(1, len(i) + 1):
#             sliced = i[:j]
#             #print(sliced)
#             pre_dic[sliced] = pre_dic.get(sliced, 0) + 1
#             #print(pre_dic)
#
#     max_len = 0
#     key_l = []
#     print(pre_dic)
#     for key, value in pre_dic.items():
#         if value == len(strs) and len(key) > max_len:
#             print(value, len(strs), len(key), max_len)
#             key_l = [key]
#             max_len = len(key)
#     print(key_l)
#     if key_l:
#         print(key_l)
#         return max(key_l)
#     else:
#         if len(strs) == 1:
#             return strs[0]
#         return ""
#
# longestCommonPrefix(strs)

# Python program to merge two sorted linked
# lists iteratively
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Function to merge two sorted linked
# lists iteratively
def sortedMerge(head1, head2):
    # Create a dummy node to simplify
    # the merging process
    dummy = Node(-1)
    print(dummy)
    curr = dummy
    print(curr)

    # Iterate through both linked lists
    while head1 is not None and head2 is not None:
        # Add the smaller node to the merged list
        if head1.data <= head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next

    # If any list is left, append it to the merged list
    if head1 is not None:
        curr.next = head1
    else:
        curr.next = head2

    # Return the merged list starting from
    # the next of dummy node
    return dummy.next


def printList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    # First linked list: 5 -> 10 -> 15 -> 40
    head1 = Node(5)
    head1.next = Node(10)
    head1.next.next = Node(15)
    head1.next.next.next = Node(40)

    # Second linked list: 2 -> 3 -> 20
    head2 = Node(2)
    head2.next = Node(3)
    head2.next.next = Node(20)

    res = sortedMerge(head1, head2)

    printList(res)


