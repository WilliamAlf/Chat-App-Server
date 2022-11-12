from termcolor import colored

def prompt_error(error):
    print(colored(error.toString(), "red"))

def prompt_success(prompt, data="", end=""):
    print(colored(f" [{prompt.upper()}] {data} {end}", "green"))

def prompt_status(prompt, data="", end=""):
    print(colored(f" [{prompt.upper()}] {data} {end}", "cyan"))