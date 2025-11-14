#here i am defining the conversion rate
dollar_to_naira_rate = 1500
#here i would request for the USD amount
dollar = int(input("Enter dollar amount you want to convert: "))
#conversion calculation
conversion_calculation = dollar * dollar_to_naira_rate
converted_amount = f"{conversion_calculation:.2f} NGN"
#print converted amount
print(f"Converting ${dollar:,.2f} at a rate of {dollar_to_naira_rate:,.2f} NGN/USD.")
print(f"The converted amount is: {converted_amount}")