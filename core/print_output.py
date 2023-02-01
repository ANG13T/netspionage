import configparser
from termcolor import colored

# Available Colors
colors = ["green", "red", "blue", "yellow", "magenta", "cyan", "white", "light_grey", "dark_grey", "light_red", "light_green", "light_yellow", "light_blue", "light_magenta", "light_cyan", "black"]

def print_output(text):
    config = configparser.ConfigParser()
    config.read('configuration.ini')
    log_text = config.get('Settings', 'LogToTextFile')
    print(colored(text, get_print_color()))
    if log_text == "True":
        with open("output.txt","a") as f:  # appends to file and closes it when finished
            print(text, file=f)

def print_input(text):
    return input(colored(text, get_print_color()))

def get_print_color():
    config = configparser.ConfigParser()
    config.read('configuration.ini')
    color = config.get('Settings', 'Color').lower()
    set_color = "green"
    if color in colors:
        set_color = color
    return set_color
