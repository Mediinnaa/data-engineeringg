store = input("Enter store name: ")

product1 = input("Enter first product name: ")
price1 = float(input("Enter first product price: "))
quantity1 = int(input("Enter first product quantity: "))

product2 = input("Enter second product name: ")
price2 = float(input("Enter second product price: "))
quantity2 = int(input("Enter second product quantity: "))

product3 = input("Enter third product name: ")
price3 = float(input("Enter third product price: "))
quantity3 = int(input("Enter third product quantity: "))

discount = float(input("Enter discount percentage: "))

revenue1 = price1 * quantity1
revenue2 = price2 * quantity2
revenue3 = price3 * quantity3

gross_revenue = revenue1 + revenue2 + revenue3
total_products = quantity1 + quantity2 + quantity3
discount_amount = gross_revenue * discount / 100
revenue_after_discount = gross_revenue - discount_amount
vat = revenue_after_discount * 18 / 100
final_revenue = revenue_after_discount + vat
average_revenue = final_revenue / total_products

print("\n========== DAILY SALES REPORT ==========")
print("Store:", store)
print(f"\nProduct 1: {product1}")
print(f"Price: {price1:.2f} EUR")
print("Quantity:", quantity1)
print(f"Revenue: {revenue1:.2f} EUR")

print(f"\nProduct 2: {product2}")
print(f"Price: {price2:.2f} EUR")
print("Quantity:", quantity2)
print(f"Revenue: {revenue2:.2f} EUR")

print(f"\nProduct 3: {product3}")
print(f"Price: {price3:.2f} EUR")
print("Quantity:", quantity3)
print(f"Revenue: {revenue3:.2f} EUR")
print("\n----------------------------------------")
print("Total Products Sold:", total_products)
print(f"Gross Revenue: {gross_revenue:.2f} EUR")
print(f"Discount ({discount}%): {discount_amount:.2f} EUR")
print(f"Revenue After Discount: {revenue_after_discount:.2f} EUR")
print(f"VAT (18%): {vat:.2f} EUR")
print(f"\nFINAL REVENUE: {final_revenue:.2f} EUR")
print(f"Average Revenue Per Item: {average_revenue:.2f} EUR")
print("========================================")
