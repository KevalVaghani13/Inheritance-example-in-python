s = input("Enter a string : ")
print(s.find("a"))
print(s.endswith("t"))
print(s.index("k"))
print(s.isdigit())
print(s.islower())
print(s.isspace())
print("_".join(s))
print(s.ljust(10,"/"))
print(s.lstrip())
print(max(s))
print(min(s))
print(s.replace("t","T"))
print(s.rfind("h"))
print(s.rindex("a"))
print(s.rjust(10,"/"))
print(s.startswith("a"))
print(s.swapcase())
print(s.upper())
print(s.isdecimal())





fact = 1
def factorialnumber(x):
    if(x<0):
        print("sorry,negative factorial not exist.")
    elif(x==0):
        print("factorial is 1")
    else:
        # fact = 1
        # global fact
        for i in range(1,x+1):
            fact = fact * i
        print(fact)
factorialnumber(5)




x = int (input("enter number:"))
sum = 0
for i in range(1,x+1):
    sum = sum + i
print(sum)
