sale_amount=float(input("Enter the price of the sale: "))
actual_amount=float(input("Enter the actual amount of the product: "))

if (sale_amount>actual_amount):
    print("The Profit is",(sale_amount-actual_amount))

else:
    print("there is no Profit")