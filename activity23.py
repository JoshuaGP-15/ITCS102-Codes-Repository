#animehe
shonen = []
isekai = []
romance = []
comedy = []



while True:
    ans = input('Do you read or watch anime?---yes / no').lower

    if ans == 'yes':
        print('What kind do you read or watch?')
        print('1 shonen \n2 Isekai\n3 Romance\n4 Comedy')

        choice = int(input('Your choice'))
        if choice == 1:
            print('shonen')
            title = input('title of the anime?')
            shonen.append(title)
            print('Lists of shonen')
            cont = input('will you continue?')
       
        elif choice == 2:
            print('isekai')
            title = input('title of the anime?')
            isekai.append(title)


    else:
        print('enk')
