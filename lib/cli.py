# lib/cli.py
from models.author import Author
from helpers import (
    exit_program,
    list_authors, 
    author_menu_choice
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            submenu_list_authors()
        else:
            print("Invalid choice")

def submenu_list_authors():
    while True:
        print("Select an author using it's index number:")
        list_authors()
        choice = input("> ")
        author = Author.find_by_id(choice)
        if author:
            print(f"Name: {author.name}, Age: {author.age}")
        elif choice == "0":
            break
        else: 
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all authors")

def author_menu():
    print ("PLease select and option:")
    print ("0. Go back to the main menu")
    print ("1. Add a book")
    print ("2. Update a book")
    print ("3. See all books by author")
    print ("4. Exit the program")




if __name__ == "__main__":
    main()
