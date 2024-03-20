def encode(password):
    if not password.isdigit() or len(password) != 8:
        return "Invalid password. Please enter an 8-digit password containing only numbers."

    encoded_password = ''.join(str((int(char) + 3) % 10) for char in password)
    return encoded_password


def main():
    while True:
        print("\nPassword Encoder")
        print("1. Encode a password")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            password_to_encode = input("Enter an 8-digit password to encode: ")
            encoded_password = encode(password_to_encode)
            print(f"Encoded password: {encoded_password}")
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 to encode a password or 2 to exit.")


if __name__ == "__main__":
    main()
