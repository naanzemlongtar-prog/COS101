#Program: Student Weekly Expense Calculator
#Purpose: To calculate students weekly expenses.



#Input
student_name = input("Rita")
daily_transport_cost = float(input("1000(NGN):"))
daily_feeding_cost = float(input("1500(NGN):"))
days_on_campus = int(input("5:"))
other_weekly_expenses = float(input("2000(NGN):"))


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
