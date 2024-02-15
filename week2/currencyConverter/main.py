usd_to_euro_rate = 0.85
usd_to_gbp_rate = 0.73
eur_to_usd_rate = 1.09
eur_to_gbp_rate = 0.86
gbp_to_usd_rate = 1.27
gbp_to_euro_rate = 1.16

input_currency = ""
unit_to_convert = ""

currency_amount = 0
result = 0

print("\nSelect the number of the currency you have:")
print("1- USD\n2- EUR\n3- GBP")
input_currency = input(": ").upper()

print("\nSelect the number of the currency you want to convert:")
print("1- USD\n2- EUR\n3- GBP")
unit_to_convert = input(": ").upper()

currency_amount = float(input("Enter the amount: "))

if input_currency == "1" and unit_to_convert == "2":
    result = currency_amount * usd_to_euro_rate
elif input_currency == "1" and unit_to_convert == "3":
    result = currency_amount * usd_to_gbp_rate
elif input_currency == "2" and unit_to_convert == "1":
    result = currency_amount * eur_to_usd_rate
elif input_currency == "2" and unit_to_convert == "3":
    result = currency_amount * eur_to_gbp_rate
elif input_currency == "3" and unit_to_convert == "1":
    result = currency_amount * gbp_to_usd_rate
elif input_currency == "3" and unit_to_convert == "2":
    result = currency_amount * gbp_to_euro_rate
else:
    print("\nUnsupported currency. Exiting...")

print("\nYour currency after conversion:", result)