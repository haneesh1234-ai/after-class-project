# AMB TICKET COUNTER
counter = int(input("""
pls inform your age to us so we can allow you to the movie if your age group allows (U/A 16+) : """))
if counter >= 16:
    ticket = input("do you have a ticket? (yes/no) : ")
    if ticket == "yes":
        print("you are allowed to watch the show pls depart to your screen number and hope you have a great time 😃")
    elif ticket == "no":
        VIP = input("do you have vip subscription at AMB 🎟 : ")
        if VIP == "yes":
            print("you may enter")
        else:
            print("sorry you are not allowed 😓")
    else:
        print("sir pls speak english")
else:
    VIP2 = input("do you have GOLDEN VIP+ SUBSCRIPTION : ")
    if VIP2 == "yes":
        print("you may enter")
    else:
        print("sorry you are under age 🚫")