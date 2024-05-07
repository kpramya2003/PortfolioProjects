
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    "1": "•----",
    "2": "••---",
    "3": "•••--",
    "4": "••••-",
    "5": "•••••",
    "6": "-••••",
    "7": "--•••",
    "8": "---••",
    "9": "----•",
    "0": "-----",
    ' ': '/'
}


def text_to_morse(text_code):
    output = [MORSE_CODE_DICT.get(char) for char in text_code]
    return output


def morse_to_text(morse_code):
    output = ''
    for char in morse_code.split():
        for (key, value) in MORSE_CODE_DICT.items():
            if char == value:
                output += key
                break
    return output.strip()


option = int(input('Enter your options  1.Text to Morse 2.Morse to text \n'))
if option == 1:
    user_input = input("Enter the string and number you wish to convert into Morse_code characters\n").upper()
    morse = text_to_morse(user_input)
    print(morse)
elif option == 2:
    user_input = input("Enter the Morse code character you wish to convert into text between spaces\n")
    text = morse_to_text(user_input)
    print(text)

