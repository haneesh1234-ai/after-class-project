shanks = input("""
Do you want to print a countdown?
If yes, enter 'yes' in lowercase: """)

if shanks == "yes":
    zoro = int(input("Starting value: "))
    luffy = int(input("Ending value: "))

    if zoro < 100000000000 and luffy < 100000000000:
        for num in range(zoro, luffy, -1):
            print(num)
    else:
        print("""
              
              eh you will die without patience before the count down ends only da
               chill , chill a little 
              and get lost i am not doing that much to much get lost.""")
else:
    print("Have a nice day")