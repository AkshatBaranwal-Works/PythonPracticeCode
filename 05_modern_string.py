# A small tool to analyze any text
text = "  python is AWESOME  "

# 1. Clean and fix the formatting
clean_text = text.strip().capitalize()

# 2. Extract specific parts (Slicing)
first_word = clean_text[:6]  # "Python"
last_word = clean_text[-7:]  # "Awesome"

# 3. Quick stats
length = len(clean_text)
word_count = len(clean_text.split())

# 4. Display results using an f-string
print(f"Original: '{text}'")
print(f"Fixed: '{clean_text}'")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"The string is {length} characters long and has {word_count} words.")

# Bonus: Reverse it!
print(f"Reverse version: {clean_text[::-1]}")
