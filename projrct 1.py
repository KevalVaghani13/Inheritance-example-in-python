s1 = input("enter your name : ")
print(s1,", welcome to our program.")

a = int(input("would you like to join our car diving school(1(yes) / 0(no)) : "))

match a:
    case 0:
        print("have a good day.")
    

    case 1:
        print("sit in car and wear seat belt.")

s = int(input("choose between (0 for reverse / 1 for forward) : "))
match s:
    case 0:
        print("car is going back.")
    case 1:
        print("car is going forward.")

a = int(input("choose (0 for stop / 1 for accelarate / 2 for shift gear in neutral) : "))
match a:
    case 0:
        print("car is stop now")
    case 1:
        print("speed is accelareted")
    case 2:
        print("car is in neutral.")

x = int(input("type 1 for raise speed / 2 for apply brake : "))
match x:
    case 1:
        print("now speed is 40km/h")
    case 2:
        print("speed is decrease.")
 
print("thank you")

