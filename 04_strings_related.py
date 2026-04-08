# Akshat's String Exploration

# 1. Multi-line Strings (The Triple Quote)
poem = """Twinkle twinkle little star,
How I wonder what you are."""

# 2. String Concatenation (Joining strings)
first_name = "Akshat"
last_name = "Baranwal"
full_name = first_name + " " + last_name
print(f"User: {full_name}")

# 3. String Slicing [Start : Stop : Step]
word = "Amazing"
print(word[0:3])   # First three: Ama
print(word[::2])   # Every second letter: Azn

# 4. Common Methods
text = "   python is great   "
print(text.strip().title())  # Cleans spaces and Capitalizes: "Python Is Great"
print(text.replace("great", "awesome")) # Swap words

# 5. Escaping Characters
# Using \n for a new line and \t for a tab
print("Learning Python:\n\t- Easy\n\t- Fun")