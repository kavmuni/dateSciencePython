def insertionSort(list1):
    """
    :param list1: Parameter is to given as a list
    :return: Returns a list which is sorted in ascending order
    """
    for i in range(1, len(list1)):
        print(f"iteration {i}")
        pos = list1[i]
        print(f"pos: {pos}")
        j = i - 1
        print(f"j: {j}")
        while j >= 0 and pos < list1[j]:
            print("inside while loop")
            print(f"list1: {list1}")
            list1[j + 1] = list1[j]
            print(f"list1[j+1]: {list1[j + 1]}")
            print(f"list1[j]: {list1[j]}")
            j = j - 1
            print(f"j: {j}")
        list1[j + 1] = pos
        print(f"list1[j+1]: {list1[j + 1]}")
        print(f"pos: {pos}")
        print(f"list1: {list1}")
        print("****************")
    print(list1)
    return list1