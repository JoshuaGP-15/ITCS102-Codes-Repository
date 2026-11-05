for y in range(5):
    for x in range(5):
        if y == 0 or x == 0 or y == 4 or x == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
