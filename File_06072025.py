# Control statements in Python
# if, else, elseif

# x = 0
# if x > 0:
#     print("positive")
# elif x == 0:
#     print("zero")
# else:
#     print("Negative")

studentScore = int(input("Please input your mark: "))
print(studentScore)
if studentScore > 90:
    print("The score is in S grade")
elif studentScore <= 90 and studentScore > 70:
    print("The score is in A grade")
elif studentScore <= 70 and studentScore > 50:
    print("The score is in B grade")
elif studentScore <= 50 and studentScore > 40:
    print("The score is in C grade")
else:
    print("The score is in D/E grade")
"""
45
The score is in C grade

86
The score is in A grade

89
The score is in A grade
"""