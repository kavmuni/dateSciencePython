class Solution:
    def countAndSay(self, n: int) -> str:
        print(f"value of n is {n}")
        if n == 0:
            return -1
        if n == 1:
            return "1"
            # why function is NOT coming out here when I give n > 1
        # I am returning a string necessarly
        prev = self.countAndSay(n - 1)
        print(f"prev: {prev}")
        res, i = "", 0
        while i < len(prev):
            print(f"i: {i}")
            count = 1
            print(f"i+1: {i + 1} and len(prev): {len(prev)}")
            while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                print(f"i+1: {i + 1} and len(prev): {len(prev)} and prev[i] = {prev[i]} and prev[i + 1]: {prev[i + 1]}")
                i += 1
                count += 1
            res += str(count) + prev[i]
            print(f"value of res = {res}")
            i += 1
        return res

sol=Solution() # Create an instance of the Solution class
res = sol.countAndSay(2) # Pass a value for 'n'
print(res)