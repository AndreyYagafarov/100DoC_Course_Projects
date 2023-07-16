from morse import morse
# A space is put between letters and three spaces are put between words (instead of a space)

def morse_to_text(text_enc):
    list_temp = text_enc.split("  ")
    for idx, val in enumerate(list_temp):
        list_temp[idx] = val.split()

    text_dec = ""

    for i in list_temp:
        for j in i:
            text_dec += list(morse.keys())[list(morse.values()).index(j)]
        text_dec += " "
    return text_dec


def text_to_morse(text_dec):
    text_enc = ""
    for i in text_dec:
        if i == " ":
            text_enc += "  "
        else:
            text_enc += morse[i] + " "

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
        print(f"The encoded text is:\n{text_enc}")
    elif menu == "d":
        text_enc = input("Please enter the text for decoding:\n").lower()
        text_dec = morse_to_text(text_enc)
        print(f"The decoded text is:\n{text_dec}")
    elif menu == "q":
        to_continue = False
    else:
        print("I am sorry, I do not recognize the command")
    # prompt = input("Would you like to perform another operation (Y/N?").lower()

print("Thank you for using the morse converter! Goodbye!")
# a = "0 ab"
# arev = "-----   .- -..."
# print(text_to_morse(a))
# print(morse_to_text(arev))

# test
# a = "random text, 123(@)"
# ad = text_to_morse(a)
# ar = morse_to_text(ad)
# print(a)
# print(ad)
# print(ar)


