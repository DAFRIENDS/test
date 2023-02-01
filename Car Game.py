command = ""

print("""Type 'HELP' to display a list of commands. """)

while True:
    command = input("> ").lower()
    if command == "start":
        print("Car has started.....")
    elif command == "stop":
        print("Car has stopped. ")
    elif command == "help":
        print("""
    start - To start the car. 
    stop - To stop the car.  
    help - To display commands. 
    quit - To exit the game. """)
    elif command == "quit":
        break
    else:
        print("I don't understand that. ")
