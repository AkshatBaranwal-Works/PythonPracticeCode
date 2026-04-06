# Negative Slicing Practice
name = "AKSHAT"

# 1. Get the last character
last_char = name[-1] 

# 2. Get the last three characters (from -3 to the end)
last_three = name[-3:]

# 3. Slice a middle section using negative numbers
# This starts at 'S' (-4) and stops before 'T' (-1)
middle_part = name[-4:-1]

# 4. Reverse the entire string (The Pro trick)
reversed_name = name[::-1]

print(f"Original: {name}")
print(f"Last character: {last_char}")      # T
print(f"Last three: {last_three}")          # HAT
print(f"Middle section: {middle_part}")    # SHA
print(f"Reversed: {reversed_name}")        # TAHSKA