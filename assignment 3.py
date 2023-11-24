# S = "python"
# print(len (S))

# s = 'programming with python'
# print(s[17:23])                    #positive index
# print(s[-6:])                      #negative index

# s = input("enter a string :")
# print(s.isalpha())
# print(s.isdigit())
# print(len (s))
# print(s.startswith("k"))
# print(s.endswith("L"))
# print(s.capitalize())  
# print(s.title())
# print(s.count("Keval"))


# h = input("enter first string : ")
# f = input("enter second string : ")
# h = h.upper() 
# f = f.upper() 

# x = sorted(h)
# y = sorted(f)
# if(x == y):
#         print(h + " and " + f + " are anagram.")
# else:
#         print(h + " and " + f + " are not anagram.")


k = input("enter a string : ")
x = k[0]
y = k[-1]
reverse = y + k[1:-1] + x
print("After Swap : ",reverse)
    