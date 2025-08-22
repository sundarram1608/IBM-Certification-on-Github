# Shipping Cost Calculator
print("Welcome to the Shipping Cost Calculator!")

rate = 500  # Shipping rate per kilogram in USD
## Input package weight
weight = float(input("Enter the package weight in kilograms: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
print("Thank you for using the Shipping Cost Calculator!")

