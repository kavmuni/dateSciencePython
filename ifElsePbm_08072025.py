def fun_if_else(n):
    # constraint # 1
    if (n < 0 or n > 100):
        return -1

    if (n%2) != 0:
        print("Weird")
    elif n>= 2 and n<=5 and n%2 == 0:
        print("Not Weird")
    elif n>= 6 and n<=20 and n%2 == 0:
        print("Weird")
    elif n > 20 and n%2 == 0:
        print("Not Weird")

    return 1

fun_if_else(24)