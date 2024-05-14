fruits = dict(apple="red", banana="yellow", orange="orange")

apple_color = fruits["apple"]
print(f"An apple is {apple_color}")

fruits["banana"] = "light yellow"
print(fruits)

del fruits["orange"]
print(fruits) 
removed_fruit = fruits.pop("banana")
print(f"Removed fruit: {removed_fruit}")

if "kiwi" in fruits:
    print("Kiwi exists in the dictionary")
else:
    print("Kiwi does not exist in the dictionary")
