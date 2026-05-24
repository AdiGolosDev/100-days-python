import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, key):
    original_text = original_text.lower()
    result = ""
    for char in original_text:
        if char == " ":
            result += " "
        elif char == ",":
            result += ","
        elif char == ".":
            result += "."
        elif char not in alphabet:
            result += "#"
        else:
            letter = alphabet[(alphabet.index(char) + key) % len(alphabet)]
            result += letter
    return result

def decrypt(original_text, key):
    original_text = original_text.lower()
    result = ""
    for char in original_text:
        if char == " ":
            result += " "
        elif char == ",":
            result += ","
        elif char == ".":
            result += "."
        elif char not in alphabet:
            result += "#"
        else:
            letter = alphabet[(alphabet.index(char) - key) % len(alphabet)]
            result += letter
    return result

def ceaser_cypher(original_text, key, encryption=True):
    if encryption:
        result = encrypt(original_text=original_text, key=key)
    else:
        result = decrypt(original_text=original_text, key=key)
    return result

again = True
while again:
    print(f"Welcome to: \n {art.logo}"
          f"\n This program encodes and decodes all messages in lower case."
          f"\nUnaffected symbols are: space, comma, dot."
          f"\nPlease note: all upper case letters and non-mentioned symbols are replaced with a hashtag #")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode":
        en = True
    elif direction == "decode":
        en = False
    else:
        print("Invalid input!")
        exit()

    text = input("Type your message:\n").lower()

    shift = int(input("Type the shift number:\n"))

    print(ceaser_cypher(text, shift, en))

    again = input("Do you want to use the program again? (type 'yes' if you do):\n").lower() == "yes"

