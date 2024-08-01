import re

def main():
    print("Welcome to the Contact Information Formatter")

    # Gather user information
    name = input("Enter your full name: ").strip()
    email = input("Enter your email address: ").strip()
    phone = input("Enter your phone number: ").strip()
    address = input("Enter your address: ").strip()

    # Validate and Format the information
    if validate_email(email) and validate_phone(phone):
        display_contact_info(name, email, phone, address)
        #save_contact_info(name, email, phone, address)
    else:
        print("Invalid email or phone number format. Please try again!")

def validate_email(email):
    # Regular Expression for validating an Email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    return False

def validate_phone(phone):
    # String all Non-Digit characters and check length
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 10:
        return True
    return False

def format_phone(phone):
    # Strip all non-digit characters and reformat
    digits = re.sub(r'\D', '', phone)
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

def display_contact_info(name, email, phone, address):

    # Format the name (capitalize the first letter of each word)
    formatted_name = name.title()

    # Format the email to lower
    formatted_email = email.lower()

    # Format the phone number(Just ensuring no leading/trailing spaces)
    formatted_phone = format_phone(phone)

    # Format the address (capitalize the first letter of each word)
    formatted_address = address.title()

    # Display the formatted information
    print("\nFormatted Contact information: ")
    print(f"Name        :{formatted_name}")
    print(f"Email       :{formatted_email}")
    print(f"Phone       :{formatted_phone}")
    print(f"Address     :{formatted_address}")

if __name__== "__main__":
    main()

