#print(list(range(1, 100, 3)))
import math
def is_prime(n):
    if n < 1:
        print(f"Give number {n} is less than to 1")
    print(f"square root of {n} is {int(math.sqrt(n))}")
    for i in range(2, int(math.sqrt(n)) + 1):
        print(i)
        print(n%i)
        if n%i==0:
            #print(f"{n} is NOT a prime number")
            return False
    return True
    #print(f"{n} is a prime number")