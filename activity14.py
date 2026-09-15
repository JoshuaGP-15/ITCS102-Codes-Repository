age = int(input("Enter your age: "))
is_employed = input('Are you employed? (True/False): ')
credit_score = int(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income: "))
has_collateral = input('Do you have collateral? (True/False): ') 

base_rate = 0.0

if age >= 21 and is_employed == True: 
    print("You passed the requirements")
    if credit_score >= 750:
        print("you have a high credit score")
    else:
        print("you have a low credit score")
else:print("you have been rejected")
