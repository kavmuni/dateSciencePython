class animal:
    def __init__(self, aniName,sound):
        self.sound = sound
        self.aniName = aniName

    def speak(self):
        print(f"{self.aniName} {self.sound} in the forest")

lion = animal("lion", "roars") # object is created here
lion.speak() # method of that object is called here to extract the output

elephant = animal("Elephant", "trumpant")
elephant.speak()

# lion roars in the forest