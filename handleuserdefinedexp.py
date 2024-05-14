def calculate(expr):
  numbers = expr.split("+")  # Split by addition first
  result = 0
  for num in numbers:
    result += float(num.split("-")[0])  # Split by subtraction, get first number
    result -= float(num.split("*")[-1]) if "*" in num else 0  # Handle multiplication if exists

  return result

user_expr = input("Enter a simple expression (e.g., 2+3-1*2): ")
try:
  result = calculate(user_expr)
  print(f"The result of '{user_expr}' is: {result}")
except ValueError:
  print("Error: Invalid expression.")
