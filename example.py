# tuple1 = ("disco",10,1.2)
# # print(type(tuple1),tuple1)

# #a:
# for index,i in enumerate(tuple1):
#     print(index,i)

# #b:
# for index,i in enumerate(tuple1):
#     print(index,type(i))

# #c:
# for index,i in enumerate(tuple1,start=-3):
#     print(index,i)

# #d:
# tuple2 = ("hard rock", 10)
# print("original tuple1:",str(tuple1))
# print("original tuple2:",str(tuple2))
# tuple3 = tuple1+ tuple2
# print(tuple3)

# #e:
# print(tuple3[0:2])

# #f:
# print(len(tuple3))

# #g:
# tuple4 = (298,36,73,75,24)
# print(sorted(tuple4))

# dict1 = {1:'apple',2:'dog',3:'vinay'}
# #a:
# print(dict1.keys())

# #b:
# print(dict1.values())

# #c:
# dict1['name']='keval'
# print(dict1)

# #d:
# dict1.pop(2)
# print(dict1)

# #e:
# key = 2
# x = list(dict1.keys())
# res = "Not Present"
# if(x.count(key) == 1):
#     res = "Present"
# print(res)


# p = {'sachin':98,'kohli':78,'yuvraj':80,'dhoni':70,'bolt':20,'surya':43,'hardik':65}
# a = input("enter name of player:")
# for key,value in p.items():
#     if(key == a):
#         print(value)

# for i in sorted(p):
#     print((i,p[i]),end=" ")


print("------------------- welcome to pizzeria ------------------")
print("--------- Here only one type of pizza available --------- ")
print("------------- cheese pizza with no toppings --------------")
print("1.Small ,price of one is 200 Rs.")
print("2.Medium ,price of one is 350 Rs.")
print("3.Large ,price of one is 500 Rs.")
s = int(input("choose your order:"))
if s == 1:
    s = 'small'
    p = 200
elif s == 2:
    s = 'medium'
    p = 350
elif s == 3:
    s= 'large'
    p = 500
else:
    print("choose correct order.")

a = int(input("enter amount of size:"))

print("Your order : ")
print(a,s,"Cheese pizza with no topping.")
print("your total ammount : ",a*p)
