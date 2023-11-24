a = "loops are amazing."
for i in a:
    print(i)

# for k in range(1, 20):      # start from 1 and end with 19.
#     print(k)
# for k in range(5):      
#     print(k)

# for a in range(2, 20, 10):          # 2 is starting , 20 is last limit ,10 is gap . 
#     print(a)                        # output is 2,12  
#                                     starting from 2 and gap is 10 so calculate 10 after 2 we get 12.




#                                 ## while loop ###
# cal = 0
# while(cal <= 10 ):
#     print(cal)
#     cal= cal+1
# else:
#     print("loop is end")


#                                 # break && continue ##
# a = 0
# for a  in range(10):
#     if(a == 8):
#         break
#     print(a)              #skip the loop from 8
#     a = a+1

# b = 0
# for b in range(20):
#     if(b == 12):
#         print("skip the iteration.")
#         continue
#     print(b)
#     b = b+1



#                 # do while emulate in py ##

# x = 0
# while True:
#     print(x)
#     x = x+1
#     if(x%2 == 0):
#         break