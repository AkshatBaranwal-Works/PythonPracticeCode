# Akshat's String Practice Code
message = "  learning Python is Fun!  "

# 1. Stripping (Removing extra spaces from ends)
clean_message = message.strip()

# 2. Case Conversion
print(clean_message.upper())      # LEARNING PYTHON IS FUN!
print(clean_message.lower())      # learning python is fun!
print(clean_message.capitalize()) # Learning python is fun!

# 3. Search and Replace
# Replaces 'Fun' with 'Awesome'
new_message = clean_message.replace("Fun", "Awesome")

# 4. Splitting (Turns a string into a list)
words = clean_message.split(" ") 
# Result: ['learning', 'Python', 'is', 'Fun!']

# 5. Checking Content
print(clean_message.startswith("learn")) # True
print(clean_message.isdigit())          # False (checks if string is only numbers)

# 6. Length of string
print(len(clean_message))

# Output display
print(f"Original: '{message}'")
print(f"Cleaned: '{clean_message}'")
print(f"Modified: {new_message}")