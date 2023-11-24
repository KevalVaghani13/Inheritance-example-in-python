questions = [["1m is equals to___.", "1cm","1km","1 foot","100cm", 4],
             ["when was taj mahal opened?","1631","1548","1648","1531", 3],
             ["who was invented apple?","steve jobs","mark zuckerberg","jen comm","lery page", 1],
             ["Brass gets discoloured in air because of the presence of which of the following gases in air?","Oxygen","Hydrogen sulphide","Carbon dioxide","Nitrogen", 2],
             ["The percentage of irrigated land in India is about","45","65","35","25", 3],
             ["The only zone in the country that produces gold is also rich in iron is","North-eastern zone","North-western zone","Southern zone","None of the above", 3],
             ["Eritrea, which became the 182nd member of the UN in 1993, is in the continent of","Asia","Africa","Europe","Australia", 2],
             ["Garampani sanctuary is located at","Junagarh, Gujarat","Diphu, Assam","Kohima, Nagaland","Gangtok, Sikkim", 2],
             ["Which was the 1st non Test playing country to beat India in an international match?","Canada","Sri lanka","Zimbabwe","East Africa", 2],
             ["who is most expensive football player of 2023?", "ronaldo", "messi", "Kylian Mbappe","Erling Haaland", 3]
             ]

levels =[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000]
money = 0
for k in range(0, len(questions)):
    question = questions[k]
    
    print(f"\n\nquestion for Rs. {levels[k]}")
    print(f"\nQue. {question[k]}")
    print(f"a. {question[1]}            b. {question[2]} ")
    print(f"c. {question[3]}            d. {question[4]} ")

    reply = int(input("enter your answer(1-4) or 0 to quit : "))
    if(reply == 0):
        money = levels[k-1]
        break

    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[k]}")
        if( k == 4):
            money = 10000
        elif(k == 9):
            money= 320000
        elif(k == 14):
            money= 10000000
    else:
        print("Wrong answer!")
        break

print(f"Your take home money is {money}")