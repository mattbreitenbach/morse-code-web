
LETTER_TO_MORSE_DICT = {"A": ".-", "B": "-...", "C": "-.-.",
                        "D": "-..", "E": ".", "F": "..-.",
                        "G": "--.", "H": "....", "I": "..",
                        "J": ".---", "K": "-.-", "L": ".-..",
                        "M": "--", "N": "-.", "O": "---",
                        "P": ".--.", "Q": "--.-", "R": ".-.",
                        "S": "...", "T": "-", "U": "..-",
                        "V": "...-", "W": ".--", "X": "-..-",
                        "Y": "-.--", "Z": "--..", "1": ".----",
                        "2": "..---", "3": "...--", "4": "....-",
                        "5": ".....", "6": "-....", "7": "--...",
                        "8": "---..", "9": "----.", "0": "-----",
                        ", ": "--..--", ".": ".-.-.-", "?": "..--..",
                        "/": "-..-.", "-": "-....-", "(": "-.--.",
                        ")": "-.--.-", " ": "/"}


def text_to_morse(text: str) -> str:
    """
    Converts a given text string into its corresponding Morse code representation.

    Args:
        text (str): The input string to be converted to Morse code.

    Returns:
        str: A string representing the Morse code translation of the input text, with 
             each Morse code character separated by a space. If an invalid character is 
             encountered, the function returns "0".
    """
    text = " ".join(text.split())
    text = text.upper()

    morse = ""
    for char in text:
        try:
            morse += f"{LETTER_TO_MORSE_DICT[char]} "
        except:
            return 0

    return morse[:-1]


def morse_to_text(morse: str) -> str:
    """
    Converts a Morse code string into its corresponding text representation.

    Args:
        morse (str): The input string containing Morse code, with each Morse code 
                     symbol separated by a space.

    Returns:
        str: A string representing the text translation of the input Morse code.
            If an invalid character is encountered, the function returns "0".
    """
    morse_list = morse.split(" ")

    text = ""
    for morse_letter in morse_list:
        try:
            letter = {
                i for i in LETTER_TO_MORSE_DICT if LETTER_TO_MORSE_DICT[i] == morse_letter}
            text += str(list(letter)[0])
        except:
            return 0

    return text

