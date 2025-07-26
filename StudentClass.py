class student_class:
    school_name = "AKG public school"
    class_ = "1 std A sec"
    total_student_class = 29

    def student_info(self, name, roll_no):
        print(f"{name} is from {self.class_} of {self.school_name} having a roll number of {roll_no}. Total strength is class id {self.total_student_class}")

student = student_class()
student.student_info("Muniappan", 13)
# Muniappan is from 1 std A sec of AKG public school having a roll number of 13. Total strength is class id 29

# class animal:
#     def __init__(self, aniName,sound):
#         self.sound = sound
#         self.aniName = aniName
#
#     def speak(self):
#         print(f"{self.aniName} {self.sound} in the forest")
#
# lion = animal("lion", "roars") # object is created here
# lion.speak() # method of that object is called here to extract the output
#
# elephant = animal("Elephant", "trumpant")
# elephant.speak()