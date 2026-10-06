capitals={}
while True:
    print("1. To add")
    print("2. To read")
    choice=int(input("Press 1/2:"))
    if choice==1:
        country=input("Enter country:")
        capital=input("Enter capital:")
        capitals[country]=capital
        print("Country's capital added")
    elif choice==2:
        print(capitals)