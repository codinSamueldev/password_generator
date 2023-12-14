import random, string

### divide each ascii elements. ###
def lowercase_abecedary():
    lowercase_letters = string.ascii_lowercase

    return lowercase_letters


def uppercase_abecedary():
    uppercase_letters = string.ascii_uppercase

    return uppercase_letters


def unique_characters():
    characters = string.punctuation

    return characters


def digits_from_zero_to_nine():
    digits = string.digits

    return digits
### end of division. ###


# weak password will have just random digits.
def weak_password():
    password_list = []

    for _ in range(4):
        password = random.choice(digits_from_zero_to_nine())
        password_list.append(password)

    user_password = "".join(password_list)

    return user_password


# medium password will have a mix of random digits + lowercase letters.
def medium_password():
    password_list = []

    for _ in range(8):
        password = random.choice(digits_from_zero_to_nine() + lowercase_abecedary())
        password_list.append(password)

    user_password = "".join(password_list)

    return user_password


# strong password will have a mix of random digits + lowercase letters + uppercase letters.
def strong_password():
    password_list = []

    for _ in range(12):
        password = random.choice(uppercase_abecedary() + digits_from_zero_to_nine() + lowercase_abecedary())
        password_list.append(password)

    user_password = "".join(password_list)

    return user_password


# unhackable password will have a mix of random digits + lowercase letters + uppercase letters + unique chars.
def unhackable_password():
    password_list = []

    for _ in range(15):
        password = random.choice(uppercase_abecedary() + digits_from_zero_to_nine() + lowercase_abecedary() + unique_characters())
        password_list.append(password)

    user_password = "".join(password_list)

    return user_password


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
        print("""
                    Your password generated is: {}
                    Password strong level: weak
              """.format(password_generated))
    elif user_choice == 2:
        password_generated = medium_password()
        print("""
                    Your password generated is: {}
                    Password strong level: medium
              """.format(password_generated))
    elif user_choice == 3:
        password_generated = strong_password()
        print("""
                    Your password generated is: {}
                    Password strong level: strong
              """.format(password_generated))
    elif user_choice == 4:
        password_generated = unhackable_password()
        print("""
                    Your password generated is: {}
                    Password strong level: unhackable
              """.format(password_generated))
    else:
        raise ValueError("Invalid input.")
