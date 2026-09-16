age = int(input("Enter Your Age ---> "))
is_employed = bool(eval(input("Are you Employed? (True/False)? ---> ")))
credit_score = int(input("What is your Credit Score? ---> "))
annual_income = float(input("What is your Annual Income? ---> "))
has_collateral = bool(eval(input("Do you have collateral? (True/False) ---> ")))

base_rate = 0.0

if age >= 21 and is_employed == True:

    if credit_score >= 750: #tier 1
        print("You pass the requirements")

        if annual_income >= 100000:
            base_rate = 4.5
            print("Loyaltu discount", base_rate)

        else:
            base_rate = 5.0
            print(" Approved! your rate is", base_rate)

    elif credit_score >= 600 and credit_score < 750: #tier2

        if has_collateral == True:
            base_rate = 7.0
            print(" Approved your rate", base_rate)

        elif annual_income < 40000:
            base_rate = 9.5
            print(" Approved! your rate", base_rate)

        else:
            base_rate = 8.0
            print("Approved! your rate", base_rate)
#tier 3
    else:
        print("Rejected: Credit score too low")

else:
    print("Rejected: Fails baseline criteria")
    
    

    
