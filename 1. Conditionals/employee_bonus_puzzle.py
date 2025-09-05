employee = input("Are you an employee? (yes/no): ").strip().lower()
if employee == "yes":
    experience = float(input("How many years have you worked here? "))
    if experience < 0:
        print("Invalid years of service")
    elif experience < 1:
        print("No bonus (less than 1 year of service)")
    elif experience >= 1 and experience <= 5:
        rating = input("Enter performance rating (A/B/C/D): ").strip().lower()
        if rating == "a":
            print("High bonus")
        elif rating == "b":
            print("Medium bonus")
        elif rating == "c":
            print("Small bonus")
        elif rating == "d":
            print("No bonus")
        else:
            print("Invalid rating. Please enter A, B, C, or D.")
    elif experience > 5 and experience <= 10:
        rating = input("Enter performance rating (A/B/C/D): ").strip().lower()
        if rating == "a":
            print("High bonus")
        elif rating == "b":
            print("Medium bonus")
        elif rating == "c":
            print("Small bonus")
        elif rating == "d":
            print("No bonus")
        else:
            print("Invalid rating. Please enter A, B, C, or D.")
    else:
        rating = input("Enter performance rating (A/B/C/D): ").strip().lower()
        if rating == "a":
            print("High bonus + Loyalty bonus")
        elif rating == "b":
            print("Medium bonus")
        elif rating == "c":
            print("Small bonus")
        elif rating == "d":
            print("No bonus")
        else:
            print("Invalid rating. Please enter A, B, C, or D.")
elif employee == "no":
    print("Not eligible for a bonus")
else:
    print("Invalid input. Please answer with 'yes' or 'no'.")
