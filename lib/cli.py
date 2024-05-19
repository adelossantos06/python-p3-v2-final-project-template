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
    space,
    add_book_bookmenu,
    update_book_bookmenu,
    delete_book_bookmenu
    
)


def main(author=None):
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            space()
            add_update_delete_submenu()
            space()
        elif choice == "2":
            book_menu(author)
        elif choice == "3":
            exit_program()
        else:
            space()
            print("Invalid input")
            space()

def submenu_list_authors():
    while True:
        space()
        print("Select an author to see details:")
        print("0. Go back to the main menu")
        authors = list_authors()
        if not authors:
            return
        space()
        
        choice = int(input("> "))
        
        if choice > len(authors):
            space()
            print("Invlid input")
            space()
            return
        
        author = authors[int(choice) -1]
        
        if choice == 0:
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
    space()
   

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
        elif choice == "4":
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
            space()
            print("Invalid input")
            space()



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
            print("Invalid input")
            space()

def book_menu(author=None):
    while True:
        space()
        print("Select an option: ")
        print("1. List all books")
        print("2. Add a book")  
        print("3. Update a book")   #TODO
        print("4. Delete a book")   #TODO
        print("5. Go back to the main menu")   #TODO
        print("6. Exit program")    
        space()
        choice = input("> ")

        if choice == "1":
            space()
            list_all_books()
            space()
        elif choice == "2":
            space()
            add_book_bookmenu(author)
            space()
        elif choice == "3":
            space()
            update_book_bookmenu(author)
            space()
        elif choice == "4":
            space()
            delete_book_bookmenu(author)
            space()
        elif choice == "5":
            main(author)
        elif choice == "6":
            exit_program()
        else:
            space()
            print("Invalid input")

if __name__ == "__main__":
    main()

