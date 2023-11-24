class Bird:
    def move(self):
        return "Bird can fly"

class Fish:
    def move(self):
        return "Fish can swim"

class Hybrid(Fish,Bird): 
    pass

def move_animal(animal):
    return animal.move()

bird = Bird()
fish = Fish()
hybrid = Hybrid()

print(move_animal(bird))   
print(move_animal(fish))   
print(move_animal(hybrid))  ##only fish class is execute because their is no super keyword.
