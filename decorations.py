from colorama import init, Fore, Style

init() #Only for windows to support for cmd ANSI escape, for colorama

def title():
    print("\n")
    print(Fore.LIGHTBLUE_EX + "|||||||  |||||||  |||||    |||||||        |||||||  ||   ||  |||||    |||||||  |||||||  ||   ||")
    print(Fore.LIGHTBLUE_EX + "||       ||   ||  ||   ||  ||             ||   ||  ||   ||  ||   ||    |||      |||     || ||")
    print(Fore.LIGHTBLUE_EX + "||       ||   ||  ||   ||  |||||     --   |||||||  ||   ||  ||   ||    |||      |||       | ")
    print(Fore.LIGHTBLUE_EX + "||       ||   ||  ||   ||  ||             ||   ||  ||   ||  ||   ||    |||      |||     || ||")
    print(Fore.LIGHTBLUE_EX + "|||||||  |||||||  |||||    |||||||        ||   ||  |||||||  |||||    |||||||    |||    ||   ||")
    print("\nCreated by https://github.com/I-am-Rudy\n" + Style.RESET_ALL)