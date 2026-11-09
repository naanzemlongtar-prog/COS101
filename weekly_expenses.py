#Program: Student Weekly Expense Calculator
#Purpose: To calculate students weekly expenses.



#Input
student_name = input("Enter student's name:")
daily_transport_cost = float(input("Enter daily transport cost(NGN):"))
daily_feeding_cost = float(input("Enter daily feeding cost(NGN):"))
days_on_campus = int(input("Enter number of days on campus:"))
other_weekly_expenses = float(input("Enter other weekly expenses(NGN):"))


#Process
Transporttotal = daily_transport_cost * days_on_campus


Feedingtotal = daily_feeding_cost * days_on_campus


Weeklytotal = Transporttotal + Feedingtotal + other_weekly_expenses




#Output
print("WEEKLY EXPENSE SUMMARY")
print("Student:", student_name)
print(f"Transport total: NGN (Transporttotal:,.2f)")
print(f"Feeding total: NGN (Feedingtotal:,.2f)")
print(f"Other weekly expenses: NGN (Otherweeklyexpenses:,.2f)")
print(f"Weekly total: NGN (Weeklytotal:,.2f)")
