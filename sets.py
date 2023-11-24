# sets be like list.
# sets are unordered.
# sets cannot give repeted value.
# sets are defind by {}.
# s = {1,3,2,4,3}
# print(s)

# info = {"ashok", 1,34,53,2}
# print( info)

# quick quiz : create a null set.
# s = {}
# print(type(s))     # it's dict 

# s = set()
# print(type(s))    # now it's null set.

                           
                           
                           
                                     # set methods #
x = {2,3,6,8,9}
y = {1,3,4,6,5}
# print(x.union(y))
# print(x.intersection(y))

# x.update(y)
# print(x,y)

# z = x.symmetric_difference(y)
# print(z)

# z = x.difference(y)      # x - y
# print(z)
# z = y.difference(x)      # y - z
# print(z)

# s = x.isdisjoint(y) 
# print(s)             # when two sets are totally different return true 

# a = x.issuperset(y)    # when one set elemetns already in another set its called super set.
# print(a)

# a = x.issubset(y)    # when one set elemetns already in another set its called super set.
# print(a)

# x.add("vk")    
# print(x)

# x.remove(2)
# print(x)

z = x.pop()     # show random items.
print(z)

z = x.clear()
print(z)