# a =[1,2,3, "keval", True]
# print(a)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[-3])    #it is negative index. convert into positive index total length of list + (-3) = 2.
                                                                            # on index 2 value is 3.


# if 2 in a:
#     print('yes')
# else:
#     print('no')


        # same concept in stirng like below:
# if "kev" in "keval":
#     print("yes")
# else:
#     print("no")

# print(a[1:-2])
# print(a[1:-3:2])     #jumpindex like strings


        # list comperhensive
j = [i for i in range(5)]
print(j)

# j = [i*i for i in range(5)]
# print(j)




                                            ## list method ##

# k = [32,43,2,54,6,4]
# print(k)

# k.append(76)
# print(k)

# k.sort()
# print(k)

# k.sort(reverse=True)
# print(k)

# k.reverse()
# print(k)

# print(k.index(2))
# print(k.count(4))          ## count repetation of element.

# e = k.copy()
# e[0] = 0
# print(k)

# m =[1,2,36,54,85]
# l=k+m
# print(l)



                                            ## tuples ##
#tuples are not change like list and string.
#one element in tuples shown like (1,).

# tup = (5,4,6, "green")
# print(type(tup),tup

# tup = (5)
# print(type(tup),tup)

# tup = (5,)
# print(type(tup),tup)

## important note every list method apply on Tuples as well but Tuple never change.


                            
                            
                            ## manipulating Tuples ## 

#if you change in Tuple you want to convert into list.

# s = (23,43,5,12,8)
# temp = list(s)             #temporary convert into list.
# temp.append(3)             #add item
# temp.pop(2)                #remove item
# temp[2] = 35               #change item
# s = tuple(temp)            #convert into Tuple
# print(s)