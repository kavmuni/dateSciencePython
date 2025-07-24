def binarySearch(list1, find_):
    """
    This function is used to use describe the Binary search and its time complexity
    :param list1:
    :param find_:
    :return:
    """
    print(type(list1))
    #if type(list1) == "<class 'list'>":
    left = 0
    right = len(list1) - 1
    print(left, right)
    while left <= right:
        mid = (left + right) //2
        print(mid, list1[mid],"test")
        if list1[mid] == find_:
            return mid
        elif list1[mid] < find_:
            left = mid + 1
        else:
            right = mid - 1
    return -1

ind = binarySearch([1,3,5,7,9], 3)
print(f"index is {ind}")