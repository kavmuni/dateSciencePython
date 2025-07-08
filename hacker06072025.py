list1 = []
N = 12
for i in range(N):
    if i == 0:
        list1.append(5)
    elif i == 1:
        list1.append(10)
    elif i == 3:
        list1[0] = 6
    elif i ==4:
        print(list1)
    elif i == 5:
        list1.remove(6)
    elif i == 6:
        list1.append(9)
    elif i == 7:
        list1.append(1)
    elif i == 8:
        list1.sort()
        
