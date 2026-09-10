import getpass
username = 'bebemo143'
password = 'password124'

u = input("Enter your Username ---")
p = getpass.getpass("Enter your Password ---")

if username == u and p == password :
          print('Acces Allowed')
else :
          print('Acces Denied')
