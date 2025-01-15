command = ""
car_start=False
#while command !="quit":
while True: #true means it will execute until break statement
    command = input('> ').lower()
    if command == "help":
        print("""        
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == 'start':
        if not car_start:
            print("CAr stARTED... READY TO GO!")
            car_start = True
        else:
            print("car has already started")
    elif command == 'stop':
        if not car_start:
            print('car is already stopped')
        else:
            car_start = False
            print("cat has  stopped")
    elif command == "quit":
        break
    else:
        print("I dont understand that")

