import os
import decorations as dec
import extensions as e
from colorama import init, Fore, Style

init()

def get_file_language(file):
    _, ext = os.path.splitext(file)
    return e.language_extensions.get(ext, 'Unknown')


def get_directory_info(directory):
    file_info = {}

    for root, _, files in os.walk(directory):
        for file in files:
            language = get_file_language(file)
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            if language not in file_info:
                file_info[language] = {'total_files': 0, 'total_size': 0}

            file_info[language]['total_files'] += 1
            file_info[language]['total_size'] += file_size

    return file_info


def display_file_info(file_info):
    print("\n------------------------------------------------------------------------------------------------")
    print(f"{'File-Lang':<30}{'|':<10}{'Size (bytes)':<25}{'|':<10}{'Total Files':<20}|")
    print("------------------------------------------------------------------------------------------------")
    for lang, info in file_info.items():
        print(f"{lang:<30}{'|':<10}{info['total_size']:<25}{'|':<10}{info['total_files']:<20}|")
    print("------------------------------------------------------------------------------------------------")

    print(Fore.LIGHTBLACK_EX + "\nThank you for using....\n")


dec.title()


if __name__ == "__main__":
    directory = input("Enter the directory path : ")
    file_info = get_directory_info(directory)


display_file_info(file_info)