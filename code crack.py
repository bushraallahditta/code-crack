
def encode(message, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in message:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            new_index = (index + shift) % 26
            new_char = alphabet[new_index]

            if char.isupper():
                new_char = new_char.upper()

            result = result + new_char
        else:
            result = result + char

    return result


def decode(message, shift):
    return encode(message, -shift)


def main():
    while True:
        print("\n1. Encode")
        print("2. Decode")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "3":
            print("thank you.")
            break

        if choice == "1" or choice == "2":
            message = input("Enter message: ")

            shift = int(input("Enter shift (0-25): "))

            if shift < 0 or shift > 25:
                print("Invalid shift!")
                continue

            if choice == "1":
                print("Encoded message:", encode(message, shift))
            else:
                print("Decoded message:", decode(message, shift))

        else:
            print("Invalid choice!")


main()
