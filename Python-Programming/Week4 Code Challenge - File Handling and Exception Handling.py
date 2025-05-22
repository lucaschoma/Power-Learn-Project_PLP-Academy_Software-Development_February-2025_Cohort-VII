# Optional: Only run this once to create input.txt
with open("input.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("Here is the second one.\n")
    file.write("Python is fun and powerful.\n")
    file.write("File operations are useful.\n")
    file.write("Last line here.\n")

# Read the contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Count the number of words
word_count = len(content.split())

# Convert all text to uppercase
upper_content = content.upper()

# Write the processed text and word count to output.txt
with open("output.txt", "w") as file:
    file.write("PROCESSED TEXT:\n")
    file.write(upper_content + "\n")
    file.write(f"\nWORD COUNT: {word_count}\n")

# Print success message
print("output.txt has been created with the processed content and word count.")
