str = "keval"
print(str[-4:-1])

       # String methods
    #strings are mutable.(never change)

s = "hi i am Keval!"
print(len (s))
print(s.upper())
print(s.lower())
print(s.isalnum())
print(s.rstrip("!"))         # USE FOR REMOVING ANYTHING FROM STRING.
print(s.replace("Keval!", "vaghani!"))
print(s.split("  "))
print(s.capitalize())            # use for first letter made capital.
print(s.center(40))
print(len(s.center(40)))
print(s.count("Keval"))

str = "joker is in circus."
print(str.isupper())
print(str.title())



            #if -else,elif statements
a = int(input("Enter your amount: ")) 

if(a>20000):
    print('you can buy car.')

elif(a==20000):
    print('your budget tight.')
    
else:
    print('you cannot buy car.')


            #nested ifelse.

a = int(input("enter your age: "))
if(a>10):
    print('Number is +ve.')
elif(a<10):
    if(a<=10):
        print("you cannot vote!")
    elif(a>18 and a<=20):
        print('you can meture')
else:
    print("you cannot drive")


                                            ## F strings ##

xyz = "every thing in {} is by {}."
name = "world"
var1 = "nature"
print(xyz.format(name,var1))          #this is old type of format string.


k1 = "genius"
var1 = "class"
print(f"you're {k1} in {var1}.")     #new type of string.
print(f"{2*30}")



