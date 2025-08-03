# https://leetcode.com/problems/generate-parentheses/description/
class possible_paranthesis:
    def possible_combinations(s):
        result = []
        #print("Coming into the body")
        # recursion function
        def get_combination(string, left, right):
            print(f"Starting Iteration - left = {left} and right = {right}, string = {string}")
            if left == 0 and right == 0:
                result.append(string)
                return
            print(f"1.{result}, left = {left}, right = {right}, string = {string}")
            if left > 0:
                get_combination(string + '(', left - 1, right)
            print(f"2.{result}, left = {left}, right = {right}, string = {string}")
            if right > left:
                get_combination(string + ')', left, right - 1)
            print(f"3.{result}, left = {left}, right = {right}, string = {string}")
            print("###############")

        print(f"********************{s}")
        get_combination('', s, s)
        print(result)
        return result


solution = possible_paranthesis
solution.possible_combinations(2)
