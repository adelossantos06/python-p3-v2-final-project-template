# lib/cli.py

from helpers import (
    exit_program,
    list_authors, 
    add_authors, 
    delete_author
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            print("***")
            list_authors()
            print("***")
        elif choice == "2":
            print("***")
            submenu_list_authors()
            print("***")
        elif choice == "3":
            if choice == "0":
                main()
            else:
                add_authors()
                print("***")
                print("Author added successfully.")
                print("***")
        elif choice == "4":
                print("***")
                print("Pick an author you would like to remove:")
                list_authors()
                print("***")
                delete_author()
                print("***")
        else:
            print("Invalid choice")

def submenu_list_authors():
    while True:
        print("***")
        print("Select an author below:")
        authors = list_authors()
        print("***")
        choice = input("> ")
        author = authors[int(choice) -1]
        
        if choice == "0":
            main()
        elif choice:
            print("***")
            print(f"Name: {author.name}, Age: {author.age}")
            print("***")
            author_menu(author)
            print("***")
            option_choice = input("> ")
            

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all authors")
    print("2. Select author from list to see the details")
    print("3. Add an author")
    print("4. Delete an author")

def author_menu(author):
    print ("PLease select an option:")
    print ("0. Go back to the main menu")
    print ("1. Add a book")
    print ("2. Update a book")
    print (f"3. See all books by {author.name}")
    print ("4. Exit the program")




if __name__ == "__main__":
    main()
