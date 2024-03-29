# Ask user for their name
name  = input("What's your name? ")

# Remove whitespace from str (if space pressed in answer, space is removed except in between multiple strings)
name = name.strip()

# Capitalize users name (all strings capitalized)
name = name.title()

# Say hello to user
print(f"hello, {name}")
