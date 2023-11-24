# # dic use for mapping.

# dic = {25:"jazz",
#        52:"yusuf",
#        82:"adnan",
#        12:"ikira",
#        10:"nh10"
#        }
# print(dic[25])

identi = {'professsion': 'doctor','name':'joy','age':'22','hight':'5.8','eligible':True}
# print(identi)

# print(identi.keys())
# for key in identi.keys():
#     print( f"the value corresponding to the key {key} is {identi[key]}")

print(identi.items())
for key, value in identi.items():
    print( f"the value corresponding to the key {key} is {value}")




                          ## dictoinaray methods ## 

#dicts are ordered.

r = { 'toll':123, 2 : 60, 3 : 100 ,4 :150, 10 : 240 }

t = {'pi': 3.14, 'het':45 , 32 :524 }

# r.update(t)
# print(r)

# r.clear()
# print(r)

# r.pop('toll')     # remove first keyword
# print(r)

# r.popitem()         # remove last keyword
# print(r)

# del r           # it shows error.
# print(r)

