alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

def encrypt(original_text, key):
    original_text = original_text.lower()
    result = ""
    for char in original_text:
        letter = alphabet[(alphabet.index(char) + key) % 26]
        result += letter
    return result

def decrypt(original_text, key):
    original_text = original_text.lower()
    result = ""
    for char in original_text:
        letter = alphabet[(alphabet.index(char) - key) % 26]
        result += letter
    return result

def ceaser_cypher(original_text, key, encryption=True):
    if encryption:
        result = encrypt(original_text=original_text, key=key)
    else:
        result = decrypt(original_text=original_text, key=key)
    return result

a = ceaser_cypher("hellomyfriendz", 9)
print(a)

b = ceaser_cypher(a, 9, False)
print(b)
