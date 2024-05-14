def fibonacci(n):
  """
  This function calculates the nth Fibonacci number.
  """
  if n < 0:
    return None  # Handle negative input
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
