# lib/cli.py

from helpers import (
    exit_program,
    list_authors, 
    add_authors, 
    delete_author,
    update_author,
    add_book_by_author,
    list_all_books,
    list_books_by_author,
    delete_book_by_author,
    update_book_by_author, 
    space
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            space()
            add_update_delete_submenu()
            space()
        elif choice == "2":
            book_menu()
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice")

def submenu_list_authors():
    while True:
        space()
        print("Select an author below to see details:")
        print("0. Go back to the main menu")
        authors = list_authors()
        space()
        
        choice = input("> ")
        author = authors[int(choice) -1]
        
        if choice == "0":
            main()
        elif choice:
            space()
            print(f"Name: {author.name}, Age: {author.age}")
            space()
        
            author_menu(author)
        else:
            print("Invalid input")
           

            

def menu():
    space()
    print("Select an option:")
    print("1. Author Menu")
    print("2. Book Menu")
    print("3. Exit program")
   

def add_update_delete_submenu():
    while True:
        print("Select an option: ")
        print("1. List authors")
        print("2. View author details") 
        print("3. Add an author")
        print("4. Delete an author")
        print("5. Update an author")
        print("6. Go back to the main menu")
        print("7. Exit the program")
        choice = input("> ")
        if choice == "1":
            space()
            list_authors()
            space()
        elif choice == "2":
            submenu_list_authors()
        elif choice == "3":
            add_authors()
            space()
            print("Author added successfully.")
            space()
        elif choice == "4":
            space()
            print("Pick an author you would like to remove:")
            list_authors()
            space()
            delete_author()
            space()
        elif choice == "5":
            update_author()
        elif choice == "6":
            main()
        elif choice == "7":
            exit_program()
        else:
            print("Invalid choice")



def author_menu(author):
    while True:
        print ("Please select an option:")
        print (f"1. Add a book by {author.name}")
        print (f"2. Update a book by {author.name}")
        print (f"3. See all books by {author.name}")
        print(f"4. Delete a book by {author.name}")
        print("5. Go back to author list")
        print("6. Exit the program")
        choice = input("> ")

        if choice == "1":
            add_book_by_author(author)
        elif choice == "2":
            update_book_by_author(author)
        elif choice == "3":
            list_books_by_author(author)
        elif choice == "4":
            delete_book_by_author(author)
        elif choice == "5":
            submenu_list_authors()
            add_update_delete_submenu()
        elif choice == "6":
            exit_program()
        else:
            space()
            print("Invalid choice")
            space()

def book_menu():
    space()
    print("Select an option: ")
    print("1. List all books")
    print("2. Exit program")
    choice = input("> ")

    if choice == "1":
        space()
        list_all_books()
        space()
    elif choice == "2":
        exit_program()
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()

