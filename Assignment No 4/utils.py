def get_user_data():
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")

    while True:
        email = input("What is your email address?")
        if "@" in email and "." in email:
            break

        else:
            print("Invalid email. Please try again!")

    return first_name, last_name, email
