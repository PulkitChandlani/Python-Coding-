def is_prime(num):
  if num <= 1:
    return False
  elif num <= 3:
    return True
  elif num % 2 == 0 or num % 3 == 0:
    return False

  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6

  return True

def print_primes(n):
    print("Prime numbers less than", n, "are:")
    for i in range(2, n + 1):
        if is_prime(i):
            print(i)

# Get user input
try:
  number = int(input("Enter a positive integer: "))
  if number < 0:
    raise ValueError("Please enter a positive number.")
except ValueError as e:
  print(f"Error: {e}")
  exit()

# Print prime numbers
print_primes(number)
