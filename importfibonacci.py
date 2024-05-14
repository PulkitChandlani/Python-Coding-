import fibonacci 

try:
  n = int(input("Enter the desired Fibonacci number (non-negative): "))
  if n < 0:
    raise ValueError("Please enter a non-negative number.")
except ValueError as e:
  print(f"Error: {e}")
  exit()

fib_number = fibonacci.fibonacci(n)

if fib_number is not None:
  print(f"The Fibonacci number at position {n} is: {fib_number}")
else:
  print("Fibonacci number is undefined for negative positions.")
