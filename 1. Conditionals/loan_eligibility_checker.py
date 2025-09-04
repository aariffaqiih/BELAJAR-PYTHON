MIN_AGE              = 21
MIN_INCOME           = 3000
MIN_CREDIT_WITH_DEBT = 700
MIN_CREDIT_NO_DEBT   = 600

print("---------------------------------------------")
print("|  Welcome to the Loan Eligibility Checker  |")
print("---------------------------------------------")

# 1. Age checking
age = int(input("Enter your age                        : "))
if age < MIN_AGE:
    print(f"Loan Rejected: You must be at least {MIN_AGE} years old.")
else:

# 2. Income checking
    income = int(input("Enter your income per month           : "))
    if income < MIN_INCOME:
        print(f"Loan Rejected: Your income must be at least ${MIN_INCOME}.")
    else:

# 3. Credit score checking
        credit = int(input("Enter your credit score               : "))
        if credit < MIN_CREDIT_NO_DEBT:
            print(f"Loan Rejected: Your credit score is too low "
                  f"(minimum {MIN_CREDIT_NO_DEBT} if no debt, "
                  f"{MIN_CREDIT_WITH_DEBT} if debt).")
        elif credit < MIN_CREDIT_WITH_DEBT:

# 4. Outstanding debt checking
            debt = input("Do you have outstanding debt (Yes/No) : ").strip().lower()
            if debt == "yes":
                print("Loan Rejected: You have outstanding debt.")
            elif debt == "no":
                print("Loan Approved!")
            else:
                print("Invalid input. Please answer Yes or No.")
        else:
            print("Loan Approved!")

print("---------------------------------------------")
print("|                 Thank You                 |")
print("---------------------------------------------")