import datetime


def listSearch(list1, n):
    # for i in range(len(list1)):
    #     #print(i, list1[i])
    #     if list1[i] == n:
    #         print(f"index of {n} is {list1.index(n)}")
    #         break
    #     else:
    #         print(f"{n} is NOT found in the list")
    print(datetime.datetime.now())
    if list1.__contains__(n): # n times it goes through array/list
        ind = list1.index(n) # n times it goes through array/list
        print(f"{n} is found in the list and its index is {ind}")
        print(datetime.datetime.now())
    else:
        print(f"{n} is NOT found in the list")

    print(datetime.datetime.now())
    try:
        print(datetime.datetime.now())
        print("Into TRY block")
        ind = list1.index(n)  # n times it goes through array/list
        print(f"{n} is found in the list and its index is {ind}")
        print(datetime.datetime.now())
    except ValueError:
        print("Not found")
    finally:
        print("Index is found or not found")
# time complexity is n+n
listSearch([1,2,3,4,5], 5)

