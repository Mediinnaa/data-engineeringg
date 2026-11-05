customer = input("Enter customer name: ")
product = input("Enter product name: ")
price = float(input("Enter product price (EUR): "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount percentage (%): "))
shipping = float(input("Enter shipping cost (EUR): "))


subtotal = price * quantity
discount_amount = subtotal * discount / 100
price_after_discount = subtotal - discount_amount
total_before_vat = price_after_discount + shipping
vat = total_before_vat * 18 / 100
total = total_before_vat + vat


print("\n======= ORDER INVOICE =======")
print("Customer:", customer)
print("Product:", product)
print(f"Unit Price: {price:.2f} EUR")
print("Quantity:", quantity)
print(f"\nSubtotal: {subtotal:.2f} EUR")
print(f"Discount ({discount}%): {discount_amount:.2f} EUR")
print(f"Shipping: {shipping:.2f} EUR")
print(f"VAT (18%): {vat:.2f} EUR")
print(f"\nTOTAL: {total:.2f} EUR")
print("=============================")
