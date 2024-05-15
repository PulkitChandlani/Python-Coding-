from math_functions import square  # Import only the square function

# Get user input
try:
  number = float(input("Enter a number: "))
except ValueError:
  print("Error: Please enter a valid number.")
  exit()

# Use the imported function
squared_number = square(number)

print(f"The square of {number} is: {squared_number}")
