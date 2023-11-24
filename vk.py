l = ['Michael Jackson',10.1,1982]
# # print(l)
# print("## POSITIVE INDEX ##")
# for index,i in enumerate(l):
#     print(index,i)
# print("## NEGATIVE INDEX ##")
# for index,i in enumerate(l,start=-3):
#     print(index,i)


l.append('keval')
print(l)
l.extend('vinay')
print(l)


l[0]="joy"
print(l)

l.pop(1)
print(l)

                 ### POP OR DEL

# del l[1]
# print(l)

a = [1, 2, 3]
b = a
print("address of a:", id(a))
print("address of b:", id(b))


s=[1,43,56,33,67,86,53,98,200]
print("even numbers are:")
for i in s:
    if(i%2==0):
        print(i)

u = [11,234,5,4,65]
s=1
for i in u:
    s = s*i
print("multiplication of all element:",s)
