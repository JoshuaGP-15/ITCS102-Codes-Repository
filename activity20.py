from getpass import getpass

u = "Joshua"
p = "Pauyo"

isLogin = False

while isLogin == False:
   

    user = input("Enter your username: ")
    password = getpass("Enter your password")

    if user == u and password == p:
        print("Login successful!")
        isLogin = True
    else:
        print("log in failed")
        isLogin = False


   
