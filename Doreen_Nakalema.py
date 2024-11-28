#Check Out System:
#When Shopping Online, One has to fill out certain details in order for the Purchase to go through.
#Here is a sample of a Check-Out form in Python.

#CUSTOMER DETAILS:

def get_fullname():
    fullname = input("Enter your full name: ")
    if fullname.isalpha():
        return fullname
    else:
        print("Invalid input. Name should only contain letters.")

def get_date_of_birth():
    dob = input("Enter your date of birth (DD/MM/YYYY): ")
    if len(dob) == 10 and dob[2] == '/' and dob[5] == '/' and dob.replace('/', '').isdigit():
        return dob
    else:
        print("Invalid input. Please enter in the format DD/MM/YYYY.")

def get_address():
    address = input("Enter your address (Street, House number, PLZ, City): ")
    return address

def get_telephone_number():
    telephone = input("Enter your telephone number: ")
    if telephone.isdigit():
        return telephone
    else:
        print("Invalid input. Please enter only numbers.")

# Print summary
def verify_information(name, dob, address, phone):
    print("\n--- Please verify the information ---")
    print(f"Name: {name}")
    print(f"Date of Birth: {dob}")
    print(f"Address: {address}")
    print(f"Telephone Number: {phone}")
    confirmation = input("Is the above information correct? (yes/no): ")
    if confirmation == "yes":
        print("Information verified. Proceeding to payment.")
    else:
        print("Please correct the information.")
        main()

# Collecting customer details
def main():
    name = get_fullname()
    dob = get_date_of_birth()
    address = get_address()
    phone = get_telephone_number()
#verifying customer details
    verify_information(name, dob, address, phone)

main()


import extension


