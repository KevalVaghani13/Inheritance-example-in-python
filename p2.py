class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Alice", 30)

print(person1 == person2)  
print(person1 != person2)  
print(person1 == person3)  
print(person1 != person3) 