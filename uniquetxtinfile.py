# Sample text content
text = """This is a sample text file. 
It contains multiple lines and some repeated words. 
We will process this text to find all the unique words."""

# Split the text into words
words = text.lower().split()  # Convert to lowercase and split

# Create an empty set to store unique words (sets don't allow duplicates)
unique_words = set()

# Add each word to the set if it's not already present
for word in words:
  unique_words.add(word)

# Print the unique words
print("Unique words in the text:")
for word in unique_words:
  print(word)
