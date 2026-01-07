morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            morse_code += char
    return morse_code.strip()

def morse_to_text(morse_code):
    words = morse_code.split(' ')
    text = ''
    for word in words:
        for letter, code in morse_code_dict.items():
            if code == word:
                text += letter
                break
        else:
            text += word
    return text

print("\nWelcome to Morse Code Translator")

while True:

    print("\n1 - Text to Morse Code Converter")
    print("2 - Morse Code to Text Converter")
    print("X - Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        text = input("\nEnter the text to convert to Morse code: ")
        morse_code = text_to_morse(text)
        print("Morse code:", morse_code)
    elif choice == '2':
        morse_code = input("\nEnter the Morse code to convert to text: ")
        text = morse_to_text(morse_code)
        print("Text:", text)
    elif choice.lower() == 'x':
        print("\nExiting the program...")
        break
    else:
        print("\nInvalid choice. Please enter 1, 2, or x.")
