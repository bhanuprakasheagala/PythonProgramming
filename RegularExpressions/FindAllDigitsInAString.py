import re

def find_digits(text):
    return re.findall(r'\d', text)

print(find_digits("My Phone number is 123-456-7890"))

# Output
['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']