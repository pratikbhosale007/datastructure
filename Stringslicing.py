#Here's a comprehensive explanation of string slicing in Python, incorporating examples:

#**String Slicing:**

# **Extracting Substrings:** Slicing allows you to extract specific portions (substrings) from a given string.
#- **Indexing:** Uses square brackets (`[]`) to specify the starting and ending indices of the desired substring.
#- **Indexing Starts from 0:** The first character in a string has an index of 0.
#- **Optional Arguments:** Slicing takes three optional arguments:
 #   - `start`: The index of the first character to include (default is 0).
#- `stop`: The index of the first character to exclude (default is the length of the string).
 #   - `step`: The number of characters to skip between each included character (default is 1).

#**Basic Slicing:**

string = "Hello, World!"

# Extract the first character
first_char = string[0]  # Output: "H"

# Extract the last character
last_char = string[-1]  # Output: "!"

# Extract a substring from index 2 to 5 (exclusive)
substring = string[2:5]  # Output: "llo"

# Extract a substring from the beginning to index 5 (exclusive)
substring = string[:5]  # Output: "Hello"

# Extract a substring from index 6 to the end
substring = string[6:]  # Output: ", World!"

#**Slicing with Step:**

string = "0123456789"

# Extract every other character
even_chars = string[::2]  # Output: "02468"

# Extract every third character, starting from index 1
every_third = string[1::3]  # Output: "147"

# Reverse the string (step of -1)
reversed_string = string[::-1]  # Output: "9876543210"

#**Key Points:**

#- Negative indices count from the end of the string.
#- If `start` is omitted, it defaults to 0.
#- If `stop` is omitted, it defaults to the length of the string.
#- If `step` is omitted, it defaults to 1.
#- Slicing creates a new string, leaving the original string unchanged.

#**Additional Examples:**

string = "Python is a powerful language"

# Extract the word "powerful"
word = string[7:14]  # Output: "powerful"

# Extract the last three characters
last_three = string[-3:]  # Output: "age"

# Extract every other character, starting from the end
reversed_every_other = string[::-2]  # Output: "n  o rwlp o h y t"