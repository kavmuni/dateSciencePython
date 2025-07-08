# Control statements in Python
# if, else, elseif

# x = 0
# if x > 0:
#     print("positive")
# elif x == 0:
#     print("zero")
# else:
#     print("Negative")

# get an input of number and check the grades
# studentScore = int(input("Please input your mark: "))
# print(studentScore)
# if studentScore > 90:
#     print("The score is in S grade")
# elif studentScore <= 90 and studentScore > 70:
#     print("The score is in A grade")
# elif studentScore <= 70 and studentScore > 50:
#     print("The score is in B grade")
# elif studentScore <= 50 and studentScore > 40:
#     print("The score is in C grade")
# else:
#     print("The score is in D/E grade")
"""
45
The score is in C grade

86
The score is in A grade

89
The score is in A grade
"""

#Marks of a student in all subject
# marks={"English": 89, "Tamil": 90, "Maths": 100, "Science": 99, "Social": 97}
# for key, value in marks.items():
#     print(key, value)
#     if value > 90:
#         print(f"{key} subject has a score of {value} and it is in S grade")
#     elif value <= 90 and value > 70:
#         print(f"{key} subject has a score of {value} and it is in A grade")
#     elif value <= 70 and value > 50:
#         print(f"{key} subject has a score of {value} and it is in B grade")
#     elif value <= 50 and value > 40:
#         print(f"{key} subject has a score of {value} and it is in C grade")
#     else:
#         print(f"{key} subject has a score of {value} and it is in D/E grade")

# count th enumber of Vowels
# str_="Inceptez"
# vowelCount=0
# vowles=["a","e","i","o","u"]
# for e in str_:
#     if e.lower() in vowles:
#         vowelCount = vowelCount+1
# print(vowelCount)

# str_ = ("Inceptez").lower()
# count = 0
# for ch in str_:
#     if ch in "ieaou":
#         count += 1
# print(count)

# import  isPrime
# number_to_check=13
# if isPrime.is_prime(number_to_check):
#     print(f"{number_to_check} is a prime number")
# else:
#     print(f"{number_to_check} is NOT a prime number")


arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
print(arr)
print("All is well")