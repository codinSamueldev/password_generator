import random, string

### divide each ascii elements. ###
def lowercase_abecedary():
    return string.ascii_lowercase


def uppercase_abecedary():
    return string.ascii_uppercase


def unique_characters():
    return string.punctuation


def digits_from_zero_to_nine():
    return string.digits   
### end of division. ###


# weak password will have just random digits.
def weak_password():
    
    return "".join(random.choice(digits_from_zero_to_nine()) for _ in range(4))


# medium password will have a mix of random digits + lowercase letters.
def medium_password():

    return "".join(random.choice(digits_from_zero_to_nine() + lowercase_abecedary()) for _ in range(8))


# strong password will have a mix of random digits + lowercase letters + uppercase letters.
def strong_password():

    return "".join(random.choice(uppercase_abecedary() + digits_from_zero_to_nine() + lowercase_abecedary()) for _ in range(12))


# unhackable password will have a mix of random digits + lowercase letters + uppercase letters + unique chars.
def unhackable_password():

    return "".join(random.choice(lowercase_abecedary() + digits_from_zero_to_nine() + uppercase_abecedary() + unique_characters()) for _ in range(15))


if __name__ == "__main__":
    user_choice = int(input("""
                    Password strong levels...
                    1) weak
                    2) medium
                    3) strong
                    4) unhackable
                    Type how strong you want your new password will be: """))

    if user_choice == 1:
        password_generated = weak_password()
        print(f"""
                    Your password generated is: {password_generated}
                    Password strong level: weak
              """)
    elif user_choice == 2:
        password_generated = medium_password()
        print(f"""
                    Your password generated is: {password_generated}
                    Password strong level: medium
              """)
    elif user_choice == 3:
        password_generated = strong_password()
        print(f"""
                    Your password generated is: {password_generated}
                    Password strong level: strong
              """)
    elif user_choice == 4:
        password_generated = unhackable_password()
        print(f"""
                    Your password generated is: {password_generated}
                    Password strong level: unhackable
              """)
    else:
        raise ValueError("Invalid input.")
    
