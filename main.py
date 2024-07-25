
def display_menu():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit

""")

def encode(password):
    encoded_value = ''
    for i in range (len(password)):
        val = int(password[i])
        val = val + 3
        val = val % 10
        encoded_value += val

    return encoded_value

    pass


# add def decode(password) below
def decode(password):
    decoded_value = ''
    for i in range(len(password)):
        val = int(password[i])
        val = val + 7
        decoded_value += str(val)[-1:]
    return decoded_value

    pass

def main():

    while True:
        encoded_password = ''
        display_menu()
        options = int(input("Please enter an option:"))

        if options == 1:
            password = input("Please enter the password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif options == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        elif options == 3:
            break



    pass





if __name__ == "__main__":
    main()






