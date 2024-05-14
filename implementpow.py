class Power:
  def __init__(self):
    pass

  def pow(self, x, n):
    if x == 0:
      if n == 0:
        return 1  # Handle 0^0 case (indeterminate) - return 1 by convention
      else:
        return 0  # Handle x^0 for x != 0
    elif x == 1:
      return 1
    elif n == 0:
      return 1
    elif n < 0:
      return self.pow(1 / x, -n)  # Handle negative exponents using 1/x^-n
    else:
      # Efficient recursive approach for positive exponents
      result = self.pow(x, n // 2)
      if n % 2 == 0:
        return result * result
      else:
        return result * result * x

# Example usage
power_calculator = Power()
result = power_calculator.pow(2, 3)
print(f"2 raised to the power of 3 is: {result}")  # Output: 2 raised to the power of 3 is: 8
