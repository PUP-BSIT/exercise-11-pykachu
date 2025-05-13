from art import tprint
from termcolor import cprint

def text_to_art():
    cprint("ASCII ART GENERATOR", "magenta")
   
    user_input = input("Please enter a word to convert: ")
   
    tprint(user_input)
    cprint("ASCII art generated!", "magenta")


