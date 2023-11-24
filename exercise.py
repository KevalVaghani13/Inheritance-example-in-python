import time
morning = "good morning, sir"
afternoon = "good after noon,sir"
evening = "good evening, sir"

x = input("enter your name sir : ")
print("welcome,", x, "sir")

hour = int(time.strftime("%H"))
min = int(time.strftime("%M"))
if 17 >= hour >= 12:
    print("it's", hour,":",min, afternoon)
elif 0 < hour < 12:
    print("its", hour,":",min, morning)
else:
    print("its", hour,":",min, evening)
