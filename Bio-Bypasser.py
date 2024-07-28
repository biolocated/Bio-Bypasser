import signal
import sys
from colorama import init, Fore, Style

init()

letters = {
    "A": "Α", "a": "α",
    "B": "Β", "b": "β",
    "C": "С", "c": "с",
    "D": "D", "d": "ԁ",
    "E": "Ε", "e": "ȩ",
    "F": "Ғ", "f": "Ғ",
    "G": "ԍ", "g": "ԍ",
    "H": "Η", "h": "һ",
    "I": "I", "i": "i",
    "J": "Ј", "j": "ј",
    "K": "Κ", "k": "κ",
    "L": "L", "l": "ӏ",
    "M": "Μ", "m": "м",
    "N": "Ν", "n": "п",
    "O": "Ο", "o": "ο",
    "P": "Ρ", "p": "р",
    "Q": "Ԛ", "q": "ԛ",
    "R": "Ŗ", "r": "ᴦ",
    "S": "Ș", "s": "ş",
    "T": "Τ", "t": "τ",
    "U": "Џ", "u": "џ",
    "V": "Ѵ", "v": "ѵ",
    "W": "Ԝ", "w": "ԝ",
    "X": "Χ", "x": "x",
    "Y": "Υ", "y": "ƴ",
    "Z": "Ζ", "z": "ᴢ"
}

def translate(string):
    translated_string = ""
    for char in string:
        translated_string += letters.get(char, char)
    return translated_string

def print_ascii_art():
    ascii_art = """
        ____  ________        ______  ______  ___   __________ __________ 
       / __ )/  _/ __ \      / __ ) \/ / __ \/   | / ___/ ___// ____/ __ \\
      / __  |/ // / / /_____/ __  |\  / /_/ / /| | \\__ \\\\__ \\/ __/ / /_/ /
     / /_/ // // /_/ /_____/ /_/ / / / ____/ ___ |___/ /__/ / /___/ _, _/
    /_____/___/\\____/     /_____/ /_/_/   /_/  |_/____/____/_____/_/ |_|
    """
    print(f"{Fore.MAGENTA}{ascii_art}{Style.RESET_ALL}\n{Fore.CYAN}--made by biolocated{Style.RESET_ALL}\n")

def ask_for_input():
    try:
        while True:
            input_text = input(f"{Fore.RED}Enter a word to translate (CTRL+C to quit): {Style.RESET_ALL}")
            translated_text = translate(input_text)
            print(f"Translated text: {translated_text}")
    except KeyboardInterrupt:
        print("\nExiting...")

print_ascii_art()
ask_for_input()
