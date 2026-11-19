#jeepney sim

route = ['Terminal','Perez Park','Pacific Mall']
passengers = []
fare = 13
seats = 6
total = 0


while True:
    print()
    print('Sakay:',passengers)
    print(len(passengers),'of',seats,'seats')
    print('1 Sakat 2 Ppriority seat  3 Para po!')
    print('4 baba pinto 5 baba sa harap')
    print('6 Seat Check 7 Balikan 8 exit')
    choice = input('Choice:')


    if choice == '1':
        if len(passengers) == seats:
            print('Puno na')
        else:
            name = input('Name:')
            passengers.append(name)
            total = total + fare
            print(name,'Boarded at the back.')
    elif choice == '2':
        if len(passengers) == seats:
            print('Puno na')
        else:
            name = input('Name:')
            passengers.insert(0,name)
            total = total + fare
            print(name,'took the priority seat.')
    elif choice == '3':
        name = input('who us getting off?')
        if name in passengers:
            passengers.remove(name)
            print(name,'bumaba')
        else:
            print('name,wala sa jeep')
    elif choice == '4':
        if len(passengers) == 0:
            print('walang tao sa jeep')
        else:
            left = passengers.pop()
            print(left,'bumababa na sa pinto')

    elif choice == '5':
        if len(passengers) == '0':
            print('The jeep is empty')
        else:
            front = passengers.pop(0)
            print(front,'Got off the front')
    elif choice == '6':
        for i in range(len(passengers)):
            print('Seat', i + 1,passengers[i])
    elif choice == '7':
        route.reverse()
        print('Route:',route)

    elif choice == '8':
        print('total fare today',total)
        break
    else:
        print('Invalid choice.')
    
