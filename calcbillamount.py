def calculate_bill_amount(quantity, price, discount_rate, tax_rate):
  # Calculate the amount before discount
  amount_before_discount = quantity * price

  # Calculate the discount amount
  discount_amount = amount_before_discount * discount_rate

  # Calculate the amount after discount
  amount_after_discount = amount_before_discount - discount_amount

  # Calculate the tax amount
  tax_amount = amount_after_discount * tax_rate

  # Calculate the total bill amount
  total_bill_amount = amount_after_discount + tax_amount

  # Return a dictionary with the calculated values
  return {
      "amount_before_discount": amount_before_discount,
      "discount_amount": discount_amount,
      "amount_after_discount": amount_after_discount,
      "tax_amount": tax_amount,
      "total_bill_amount": total_bill_amount,
  }

# Example usage
bill_details = calculate_bill_amount(2, 10.00, 0.1, 0.07)  # Quantity, price, discount rate, tax rate

# Print the bill details
print("Amount before discount:", bill_details["amount_before_discount"])
print("Discount amount:", bill_details["discount_amount"])
print("Amount after discount:", bill_details["amount_after_discount"])
print("Tax amount:", bill_details["tax_amount"])
print("Total bill amount:", bill_details["total_bill_amount"])
