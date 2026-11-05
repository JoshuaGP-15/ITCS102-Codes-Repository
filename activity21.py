sum = 0 

eh = True

while eh == True:
    a = int(input("Enter a number: "))

    if a == 0:
        print('Loop stopped')
        print('total is', sum)
        break
    else:
        sum += a
        print('total is', sum)
        continue
    

