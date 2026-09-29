age = int(input("What is your age? "))
monthly_revenue = float(input("What is your monthly revenue? "))
credit_score = int(input("What is your credit score? "))
years_business = float(input("How many years have you been doing it? "))
has_defaults = bool(input("Have you been bankrupted before?"))
collateral_name = input("What is your collateral? ")
collateral_value = int(input("What is your collateral value? "))

base_rate = 0
maximum_loan = 0

# outer baseline criteria
if age >= 21 and years_business >= 2.0 and has_defaults == False:
    print("You are eligible for loan")
    
    if credit_score >= 720:  # Tier 1
        maximum_loan = monthly_revenue * 3
        print("You have High credit score")
        print("Maximum loan is", maximum_loan)

        if monthly_revenue >= 50000:
            base_rate = 0.015
            print("Your Rate is", base_rate)
        else:
            base_rate = 0.025
            print("Base rate is", base_rate)

    elif credit_score >= 620 and credit_score < 720: #tier 2
        maximum_loan = monthly_revenue * 1.5
        print("Maximum loan is", maximum_loan)

        if years_business >= 5.0:
            base_rate = 0.02
            print("Base rate is", base_rate)
        else:
            base_rate = 0.035
            print("Base rate is", base_rate)
            #Surcharge
            if collateral_value >= maximum_loan :
                print("Collateral value is higher than maximum loan")
                
                final_rate = maximum_loan * base_rate
                
                if int(collateral_value) % 5000 != 0 :
                    final_rate += 250.00
                    print("The final rate is", final_rate)
                
                                                     
            else:
                print("Collateral value is insufficient")           

    else: #tier 3
        print("Credit score too low")
                                                                                                                  
            
else:
    print("Rejected: Failed baseline criteria")
