import re

def extract_words(text):
    return re.findall(r'\b\w+\b', text)

print(extract_words("Hello, world! This is a test code @ 04-08-2024"))
print(extract_words("@$%6 t4t t45t4"))