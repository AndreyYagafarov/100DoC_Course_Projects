from morse import morse
# A space is put between letters and three spaces are put between words (instead of a space)

is_error = False


def morse_to_text(text_enc):
    global is_error
    list_temp = text_enc.split("  ")
    for idx, val in enumerate(list_temp):
        list_temp[idx] = val.split()

    text_dec = ""

    try:
        for i in list_temp:
            for j in i:
                text_dec += list(morse.keys())[list(morse.values()).index(j)]
            text_dec += " "
    except ValueError:
        is_error = True
        print("There appears to be an error in the input. Please check")
    return text_dec


def text_to_morse(text_dec):
    global is_error
    text_enc = ""

    try:
        for i in text_dec:
            if i == " ":
                text_enc += "  "
            else:
                text_enc += morse[i] + " "
    except KeyError:
        is_error = True
        print("There appears to be an error in the input. Please check")


# the code above will always add a space at the end hence [:-1]
    return text_enc[:-1]


to_continue = True
print("This is a text based morse converter.")
print("The following conventions are used:")
print("- When encoding, a space is put between letters and three spaces are put between words (instead of a space)")
print("- The same is expected when decoding")
print("- Decoding always returns lower case")

while to_continue:

    menu = input("What would you like to do (press E for encoding, D for decoding, Q to quit: ").lower()
    if menu == "e":
        text_dec = input("Please enter the text for encoding:\n").lower()
        text_enc = text_to_morse(text_dec)
        if not is_error:
            print(f"The encoded text is:\n{text_enc}")
    elif menu == "d":
        text_enc = input("Please enter the text for decoding:\n").lower()
        text_dec = morse_to_text(text_enc)
        if not is_error:
            print(f"The decoded text is:\n{text_dec}")
    elif menu == "q":
        to_continue = False
    else:
        print("I am sorry, I do not recognize the command")
    # prompt = input("Would you like to perform another operation (Y/N?").lower()

print("Thank you for using the morse converter! Goodbye!")
