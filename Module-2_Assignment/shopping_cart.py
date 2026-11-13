
# Simple Shopping Cart Program

# Function to calculate discount
def calculate_discount(subtotal):

    if subtotal >= 5000:
        discount_rate = 0.20

    elif subtotal >= 3000:
        discount_rate = 0.10

    elif subtotal >= 1000:
        discount_rate = 0.05

    else:
        discount_rate = 0

    discount = subtotal * discount_rate

    return discount


# Take customer name
customer_name = input("Enter Customer Name: ")

# Initialize variables
subtotal = 0
products = []

# Take 3 products information
for i in range(1, 4):

    print(f"\nEnter Product {i} Information")

    product_name = input("Product Name: ")
    price = float(input("Product Price: "))

    # Store product information
    products.append((product_name, price))

    # Calculate subtotal
    subtotal += price


# Calculate discount
discount = calculate_discount(subtotal)

# Calculate final total
final_total = subtotal - discount


# Display Shopping Summary
print("\n========== Shopping Summary ==========")

print(f"Customer Name: {customer_name}")

for i, (product_name, price) in enumerate(products, start=1):

    print(f"\nProduct {i}: {product_name}")
    print(f"Price: {price:.2f}")

print("\n--------------------------------------")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Total: {final_total:.2f}")
print("======================================")

