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
    update_book_by_author
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            print("***")
            list_authors()
            print("***")
            print("Select from the options below: ")
            add_update_delete_submenu()
        elif choice == "2":
            print("***")
            submenu_list_authors()
            print("***")
        elif choice == "3":
            print("***")
            list_all_books()
            print("***")
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice")

def submenu_list_authors():
    while True:
        print("Select an author below to see details:")
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

            

def menu():
    print("Please select an option:")
    print("1. List all authors")
    print("2. Select author from list to see the details")
    print("3. List all books")
    print("4. Exit program")
   

def add_update_delete_submenu():
    print("1. Add an author")
    print("2. Delete an author")
    print("3. Update an author")
    print("4. Go back to the main menu")
    print("5. Exit the program")
    choice = input("> ")
    if choice == "1":
        add_authors()
        print("***")
        print("Author added successfully.")
        print("***")
    elif choice == "2":
        print("***")
        print("Pick an author you would like to remove:")
        list_authors()
        print("***")
        delete_author()
        print("***")
    elif choice == "3":
        update_author()
    elif choice == "4":
        main()
    elif choice == "5":
        exit_program()
    else:
        print("Invalid choice")



def author_menu(author):
    print ("Please select an option:")
    print (f"1. Add a book by {author.name}")
    print (f"2. Update a book by {author.name}")
    print (f"3. See all books by {author.name}")
    print(f"4. Delete a book by {author.name}")
    print("5. Exit the program")
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
        exit_program()


if __name__ == "__main__":
    main()

