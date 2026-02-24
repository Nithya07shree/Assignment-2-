# get user input
x = input("Enter a sentence: ")


# original sentence
print(f"Original: {x}")
# character count of sentence with spaces
print(f"Characters (with spaces): {len(x)}")
# character count of sentence without spaces
print(f"Characters (without spaces): {len(x.replace(' ',''))}")
# number of words in sentence
print(f"Words: {len(x.split())}")
# characters of the sentence converted to Uppercase
print(f"Uppercase: {x.upper()}")
# characters of the sentence converted to Lowercase
print(f"Lowercase: {x.lower()}")
# Convert original sentence to Titlecase
print(f"Title Case: {x.title()}")
# First word of the original sentence
print(f"First Word: {(x.split())[0]}")
# last word of the original sentence
print(f"Last Word: {(x.split())[-1]}")
# reversed original sentence
print(f"Reversed sentence: {x[::-1]}")