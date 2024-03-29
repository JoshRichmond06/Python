# Ask user for their name
name  = input("What's your name? ")

# Remove whitespace from str (if space pressed in answer, space is removed except in between multiple strings) & Capitalize users name (all strings capitalized)
name = name.strip().title()

# Say hello to user
print(f"hello, {name}")
