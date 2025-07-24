def process_data(fixed_arg, *args, **kwargs):
    print(f"Fixed argument: {fixed_arg}")
    print(f"Positional arguments (args): {args}, {type(args)}")
    print(f"Keyword arguments (kwargs): {kwargs}, {type(kwargs)}")

process_data("Start", 1, 2, 3, item="apple", quantity=5)

# Read about *args, **kwargs
# Single Inheritance
from animalClass import animal

class horse(animal):
    def move(self, mode):
        print(f"{self.aniName} is {mode} now")

pet = horse("horse", "Neigh")
pet.speak()
pet.move("Running")