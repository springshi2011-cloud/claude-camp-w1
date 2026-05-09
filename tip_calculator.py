# Tip Calculator

# Ask the user for the bill amount
bill_amount = float(input("Enter the bill amount: $"))

# Ask the user for the tip percentage
tip_percentage = float(input("Enter the tip percentage: "))

# Calculate the tip amount
tip_amount = bill_amount * (tip_percentage / 100)

# Calculate the total amount
total_amount = bill_amount + tip_amount

# Display the results
print(f"\nBill Amount: ${bill_amount:.2f}")
print(f"Tip Amount: ${tip_amount:.2f}")
print(f"Total Amount: ${total_amount:.2f}")