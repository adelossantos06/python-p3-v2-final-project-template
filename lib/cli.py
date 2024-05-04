# lib/cli.py

from helpers import (
    exit_program,
    list_authors
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_authors()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all authors")


if __name__ == "__main__":
    main()
