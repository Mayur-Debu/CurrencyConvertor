"""This is a currency converter program used to convert indian ruppess to any currency."""

with open("ExchangePrices.txt") as file:
    lines=file.readlines()

currency_dictonary={}                    #Currency Dictionary

for line in lines:
    parsed=line.split("\t")
    currency_dictonary[parsed[0]]=parsed[1]

amount=int(input("Enter the amount: "))
print("\nChoose one of these currency: \n")
for item in currency_dictonary.keys():
    print(item)

currency=input("Please enter the currency to convert into: ")
print(f"\n The {amount} INR in {currency} = {float(currency_dictonary[currency])*amount}")