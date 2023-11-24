def fibbonachi(d):
    if(d == 0):
      return 0
    elif (d == 1 or d == 2): 
         return 1
    else:
        return  d + fibbonachi(d-1)   #call the function in the function.
print(fibbonachi(5))

 
x = int(input("Enter the terms : "))
f=0                                         #first term of series
s=1                                         #second term of series
if(x<=0):
    print("The requested series is",f)
else:
    print(f, s , end=" ")
    for j in range(2,x):
        nextterm = f + s                           
        print(nextterm ,end=" ")
        f = s
        s = nextterm
 