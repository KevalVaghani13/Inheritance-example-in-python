# def isgreater(x,y):                                 # to create a function write def 
#     if(x>y):
#         print("X is greater than Y")                # body part
#     else:
#         print("Y is greater than X")

# x = int(input("enter x : "))
# y = int(input("enter y : "))
# isgreater(x,y)                                      # calling function



# def printtable(x,i):
#     for i in range(10):
#         print(x,"*", i+1, "=", x*(i+1) )

# i=0
# x = int(input("enter number to printtable : "))
# printtable(x,i)




                                        # function argument #

# def average(a=1,b=9):
#     print("the ave is : ", (a+b)/2)

# average()                     #default arg

# def fruit(a,b,c):
#     print("fruits are", a,b,c)

# fruit(b = "banana" , c = 'cherry' , a = 'apple')        # keyword argu. order dose't matter

# def num(a,b,c=1):
#     print("numbers are ",a,b,c)

# num(4,5)                                      #required arg. in this example by default compiler choose a= 4,b=5.


                        
# def name(*name):
#     print(type(name))
#     print("Hi",name[0], name[1])
# name("vk","ad")                               #variable length args.

# def name(**name):
#     print(type(name))
#     print("Hi",name["fname"], name["lname"])
# name(fname="keval", lname="vaghani")            # keyword arbitrary args.



# def color(red,green):
#     return "colors are "  + red + " " + green + " "
# print(color("neon," , "lime."))                       # return statements.



# i=0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
#     else:
#         print(0)


# def eoo():
#     try:
#         return 1
#     finally:
#         return 2
# k = eoo()
# print(k)



# class DemoC:
#     def __init__(self):
#         self.a = 1
#         self.__b = 1

#     def display(self):
#         return self.__b
    
# obj = DemoC()
# print(obj.__b)



h=(i for i in range(5))
print(type(h))



# import re
# txt = "planet"
# x= re.findall("^hello",txt)
# if x:
#     print(1)
# else:
#     print(0)



# def validate_email(email):
#     return '@' in email and '.' in email.split('@')[-1]
# user_email = input("Enter your email address: ")
# if validate_email(user_email):
#     print("The entered email is in proper format.")
# else:
#     print("Invalid email format. Please enter a valid email address.")


# import re
# def validate_email(email):
#     email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     if re.match(email_pattern, email):
#         return True
#     else:
#         return False
# user_email = input("Enter your email address: ")
# if validate_email(user_email):
#     print("The entered email is in proper format.")
# else:
#     print("Invalid email format. Please enter a valid email address.")






j=0
for i in range(1,6):
    j = j + i
print(j)
