def medianOf2(a, b):
    n = len(a)
    m = len(b)
    print(n, m)
    # If a[] has more elements, then call medianOf2
    # with reversed parameters
    if n > m:
        return medianOf2(b, a)
    print(f"array 1: {a}")
    print(f"Array 2: {b}")
    lo = 0
    hi = n # get the length of small array/list
    while lo <= hi:
        print(f"Printing the value of low and high {lo} and {hi}")
        mid1 = (lo + hi) // 2
        mid2 = (n + m + 1) // 2 - mid1
        print(f"Printing the value middle value: {mid1} and {mid2}")
        # Find elements to the left and right of partition in a[]
        l1 = (mid1 == 0) and float('-inf') or a[mid1 - 1]
        r1 = (mid1 == n) and float('inf') or a[mid1]
        print(f"Printing value of left1 and right1: {l1} and {r1}")
        # Find elements to the left and right of partition in b[]
        l2 = (mid2 == 0) and float('-inf') or b[mid2 - 1]
        r2 = (mid2 == m) and float('inf') or b[mid2]
        print(f"Printing value of left2 and right2: {l2} and {r2}")
        # If it is a valid partition
        if l1 <= r2 and l2 <= r1:

            # If the total elements are even, then median is
            # the average of two middle elements
            if (n + m) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2.0

            # If the total elements are odd, then median is
            # the middle element
            else:
                return max(l1, l2)

        # Check if we need to take lesser elements from a[]
        if l1 > r2:
            hi = mid1 - 1

        # Check if we need to take more elements from a[]
        else:
            lo = mid1 + 1
        print('***************')
    return 0


if __name__ == "__main__":
    a = [1, 12, 15, 26, 38]
    b = [2, 13, 17, 30, 45, 60]

    print(medianOf2(a, b))