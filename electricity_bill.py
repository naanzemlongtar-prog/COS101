# Calculate the bill using fictional tiered classroom rates.

customer_name = input("Enter the customer's name: ")
energy_kWh = float(input("Enter energy consumed in kWh: "))

if energy_kWh < 0:
    print("Invalid consumption. Energy cannot be negative.")
else:
    if energy_kWh <= 50:
        bill = energy_kWh * 50
        
    elif energy_kWh <= 150:
        bill = (50 * 50) + ((energy_kWh - 50) * 75)
        
    else:
        bill = ((50 * 50) + (100 * 75) + (energy_kWh - 150) * 100)


    print()
    print("ELECTRICITY BILL")
    print("================")
    print(f"Customer: {customer_name}")
    print(f"Energy consumed: {energy_kWh:.2f}kWh")
    print(f"Amount payable: NGN {bill:.2f}")
