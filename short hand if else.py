# a = 89
# b = 76
# print("A") if a<b else print("=") if a==b else print("B")



          ####  enumareter function

# names = ['joy','loy','vicky']
# for index, name in enumerate(names):
#     print(index,name)


names = ['joy','loy','vicky']
for index, name in enumerate(names, start=2):    ### start indexing with 2.
    print(index,name)
    if index == 2:
        print('joy is good boy.')