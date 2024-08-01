def main():
    print("Welcome to the Contact Information Formatter")

    # Gather user information
    name = input("Enter your full name: ").strip()
    email = input("Enter your email address: ").strip()
    phone = input("Enter your phone number: ").strip()
    address = input("Enter your address: ").strip()

    # Format and Display the information
    display_contact_info(name, email, phone, address)

def display_contact_info(name, email, phone, address):

    # Format the name (capitalize the first letter of each word)
    formatted_name = name.title()

    # Format the email to lower
    formatted_email = email.lower()

    # Format the phone number(Just ensuring no leading/trailing spaces)
    formatted_phone = phone

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

