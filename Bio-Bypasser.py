import signal
import sys
from colorama import init, Fore, Style

init()

letters = {
    "A": "Α", "a": "ɑ",
    "B": "Β", "b": "Ь",
    "C": "Ϲ", "c": "ϲ",
    "D": "Ꭰ", "d": "ԁ",
    "E": "Ε", "e": "е",
    "F": "Ϝ", "f": "ғ",
    "G": "Ԍ", "g": "ɡ",
    "H": "Η", "h": "һ",
    "I": "Ι", "i": "і",
    "J": "Ј", "j": "ϳ",
    "K": "Κ", "k": "κ",
    "L": "Ꮮ", "l": "ӏ",
    "M": "Μ", "m": "м",
    "N": "Ν", "n": "ո",
    "O": "Ο", "o": "о",
    "P": "Ρ", "p": "р",
    "Q": "Ⴓ", "q": "զ",
    "R": "Ꭱ", "r": "г",
    "S": "Ѕ", "s": "ѕ",
    "T": "Τ", "t": "т",
    "U": "Ս", "u": "ս",
    "V": "Ѵ", "v": "ν",
    "W": "Ԝ", "w": "ԝ",
    "X": "Χ", "x": "х",
    "Y": "Υ", "y": "у",
    "Z": "Ζ", "z": "ᴢ",
    "0": "𝟘", "1": "𝟙",
    "2": "𝟚", "3": "𝟛",
    "4": "𝟜", "5": "𝟝",
    "6": "𝟞", "7": "𝟟",
    "8": "𝟠", "9": "𝟡"
}

def translate(string):
    translated_string = ""
    for char in string:
        translated_string += letters.get(char, char)
    return translated_string

def print_ascii_art():
    ascii_art = r"""
        ____  ________        ______  ______  ___   __________ __________ 
       / __ )/  _/ __ \      / __ ) \/ / __ \/   | / ___/ ___// ____/ __ \\
      / __  |/ // / / /_____/ __  |\  / /_/ / /| | \__ \\__ \/ __/ / /_/ /
     / /_/ // // /_/ /_____/ /_/ / / / ____/ ___ |___/ /__/ / /___/ _, _/
    /_____/___/\____/     /_____/ /_/_/   /_/  |_/____/____/_____/_/ |_|
    """
    print(f"{Fore.MAGENTA}{ascii_art}{Style.RESET_ALL}\n{Fore.CYAN}--bypasser made by biolocated{Style.RESET_ALL}\n")

def ask_for_input():
    try:
        while True:
            input_text = input(f"{Fore.RED}Enter a word to bypass (CTRL+C to quit): {Style.RESET_ALL}")
            translated_text = translate(input_text)
            print(f"Translated text: {translated_text}")
    except KeyboardInterrupt:
        print("\nExiting...")

print_ascii_art()
ask_for_input()
