import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

print(validate_email("example@gmail.com")) # True
print(validate_email("5678.com"))          # False
print(validate_email("213343@.com"))       # False
print(validate_email("234234@test.in.org")) # True