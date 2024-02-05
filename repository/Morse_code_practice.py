def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    # Convert the text to uppercase to make it case-insensitive
    text = text.upper()

    morse_code_result = ""
    for char in text:
        if char in morse_code_dict:
            morse_code_result += morse_code_dict[char] + " "
        elif char == " ":
            morse_code_result += "/ "
    

    return morse_code_result

# Test cases
print(morse_translator("HELLO WORLD"))  # Output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print(morse_translator("Python"))        # Output: ".--. -.-- - .... --- -."
print(morse_translator("Morse Code"))    # Output: "-- --- .-. ... . / -.-. --- -.. ."
