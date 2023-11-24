# try:
#     x = int(input('enter your number :'))
#     a = [2,4]
#     print(a[x])

# except ValueError:
#     print("input is not number!")

# except IndexError:
#     print("invalid index!")
    
# print("program is continue.")


# finally keyword 
# imp question for finally 
# why we use finally 


# def isaverage():
#     try:
#         c = int(input('enter value of c : '))
#         b = int(input('enter value of b : '))
#         (c + b)/2
#         print((c + b)/2)
#         return 0
    
#     except ValueError:
#         print("input is not number!")
#         return 1

#     finally:
#         print("code is located in finally is always execute.")

# isaverage()




# raise custom error.
# a = input("Enter the value between 0 and 9 : ")

# if (a == "quit"):
#   print("ohk")
# elif (int(a) < 0 or int(a) > 9):
#   raise ValueError("The number should be between 0 and 9")


import re
while True:
  try:
    s = input("enter your Username (only a to z): ")
    if(s.isalpha()):
      pass
    else:
      raise ValueError("input is not alphabet!")

    d = input("enter your password :")
    if re.match(r'^[!@#$%^&*()\[\]{};:\'"<>0-9]+$', d):
      print("UserName:",s)
      print("password :",d)
      break
    else:
      raise ValueError("input is not number or special symbol!")
    
  except ValueError as e:
    print(e)
  except ValueError as er:
    print(er)





# import re  # Import the regular expression module

# # Define custom exceptions for invalid username and password
# class InvalidUsernameError(Exception):
#     pass

# class InvalidPasswordError(Exception):
#     pass

# def main():
#     while True:
#         try:
#             # Get input for the username and check if it contains only alphabets
#             username = input("Enter your username (only alphabets allowed): ")
#             if not username.isalpha():
#                 raise InvalidUsernameError("Invalid username! Username should contain only alphabets.")

#             # Get input for the password and check if it contains only special symbols and numbers
#             password = input("Enter your password (should contain only special symbols and numbers): ")
#             if not re.match(r'^[!@#$%^&*()\[\]{};:\'"<>0-9]+$', password):
#                 raise InvalidPasswordError("Invalid password! Password should contain only special symbols and numbers.")

#             # If both username and password are valid, print them and break the loop
#             print("Username:", username)
#             print("Password:", password)
#             break
        
#         except InvalidUsernameError as e:
#             # Handle the custom exception for invalid username and print the error message
#             print(e)
#         except InvalidPasswordError as e:
#             # Handle the custom exception for invalid password and print the error message
#             print(e)
# main()

