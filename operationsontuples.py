# Initial tuple
my_tuple = ("apple", "banana", "cherry")

first_fruit = my_tuple[0]
print(f"First fruit: {first_fruit}") 


updated_tuple = my_tuple[:1] + ("mango",) + my_tuple[2:]
print(f"Updated tuple: {updated_tuple}")


deleted_tuple = my_tuple[:1] + my_tuple[2:]
print(f"Deleted element (new tuple): {deleted_tuple}")  # Output: Deleted element (new tuple): ('apple', 'cherry')
