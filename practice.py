# class person:                 ## constructor
#     def __init__(self,a,occ):
#         print("Hey I am a Person.")
#         self.a = a
#         self.occ = occ

#     def info(self):
#         print(f"{self.a} is a {self.occ}")

# a = person("keval","freelancer")
# b = person("Ishan","partner")
# a.info()
# b.info()



def greet(fx):
    def mfx():
        print("Good evening.")
        fx()
        print("Thanks for using this function.")
    return mfx
    
@greet
def hello():
    print("Hello world")

def add(a,b):
    print(a+b)

hello()



def sumo():
    print("u are joker.")
    print("")