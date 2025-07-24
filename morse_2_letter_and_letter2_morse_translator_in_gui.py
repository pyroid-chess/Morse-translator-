import tkinter as tk

# Morse code to letter (for decoding)
morse_to_letter = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z", "-----": "0", ".----": "1", "..---": "2", "...--": "3",
    "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8",
    "----.": "9", ".-.-.-": ".", "--..--": ",", "..--..": "?", ".----.": "'",
    "-.-.--": "!", "-..-.": "/", "-.--.": "(", "-.--.-": ")", ".-...": "&",
    "---...": ":", "-.-.-.": ";", "-...-": "=", ".-.-.": "+", "-....-": "-",
    "..--.-": "_", ".-..-.": "\"", "...-..-": "$", ".--.-.": "@", "/": " "
}

# Letter to Morse code (for encoding)
letter_to_morse = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...",
    ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "_": "..--.-", "\"": ".-..-.", "$": "...-..-", "@": ".--.-.", " ": "/"
}

# --- Tkinter UI Setup ---
window = tk.Tk()
window.title("Morse Code Translator")
window.geometry("300x250")

tk.Label(window, text="Morse Code Translator!", font=("Arial", 14)).pack(pady=5)

entry = tk.Entry(window, width=30)
entry.pack(pady=5)

result_label = tk.Label(window, text="", wraplength=280, font=("Arial", 12))
result_label.pack(pady=10)

# Translate Morse ➜ Letter
def translate_morse_to_text():
    user_input = entry.get().split()  # Morse words are separated by space
    translated = []

    for symbol in user_input:
        if symbol in morse_to_letter:
            translated.append(morse_to_letter[symbol])
        else:
            translated.append("?")  # Unknown code

    result_label.config(text="".join(translated))

# Translate Letter ➜ Morse
def translate_text_to_morse():
    user_input = entry.get().upper()
    translated = []

    for char in user_input:
        if char in letter_to_morse:
            translated.append(letter_to_morse[char])
        else:
            translated.append("?")  # Unknown letter

    result_label.config(text=" ".join(translated))

# Buttons
tk.Button(window, text="Morse 2 Letter", command=translate_morse_to_text).pack(pady=5)
tk.Button(window, text="Letter 2 Morse", command=translate_text_to_morse).pack(pady=5)

window.mainloop()