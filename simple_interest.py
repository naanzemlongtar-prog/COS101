# Calculate the Simple Interest and Final Amount.

print("SIMPLE-INTEREST CALCULATOR")
print("==========================")

principal = float(input("Enter the principal in naira: "))
annual_rate = float(input("Enter the annual rate (%): "))
time_years = float(input("Enter the time in years: "))

interest = principal * annual_rate * time_years / 100
final_amount = principal + interest

print()
print(f"Principal: NGN {principal:.2f}")
print(f"Annual_rate: {annual_rate:.2f}%")
print(f"Time: {annual_rate:.2f} years")
print(f"Simple interest: NGN {interest:.2f}")
print(f"Final amount: NGN {final_amount:.2f}")
    

