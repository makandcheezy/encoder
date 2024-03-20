# Adam Makled
def encode(password):
    if not password.isdigit() or len(password) != 8:
        return "Invalid password. Please enter an 8-digit password containing only numbers."

    encoded_password = ''.join(str((int(char) + 3) % 10) for char in password)
    return encoded_password

# Daniyl Nguyen
def decode(encoded):
    original = ""
    for char in encoded:
        original += str(abs((int(char) + 7) % 10))
    return original

def main():
    password_to_encode = ""
    encoded_password = ""
    while True:
        print("\nPassword Encoder")
        print("1. Encode a password")
        print("2. Decode a password")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            password_to_encode = input("Enter an 8-digit password to encode: ")
            encoded_password = encode(password_to_encode)
            print(f"Encoded password: {encoded_password}")
        elif choice == "2":
            print("The encoded password is " + str(encoded_password) + ", and the original password is " + str(decode(encoded_password)))
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 to encode a password or 2 to exit.")


if __name__ == "__main__":
    main()
# Adam Makled's code