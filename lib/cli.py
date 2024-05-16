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
            #submenu_list_authors()
            add_update_delete_submenu()
            space()
            # print("***")
            # list_authors()
            # print("***")
            # print("Select from the options below: ")
            # add_update_delete_submenu()
        elif choice == "2":
            space()
            list_all_books()
            space()
            #print("***")
            #add_update_delete_submenu()
            #submenu_list_authors()
            
            #print("***")
        elif choice == "3":
            exit_program()
            #print("***")
            l#ist_all_books()
            #print("***")
        #elif choice == "4":
         #   exit_program()
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
           

            

def menu():
    space()
    print("Please select an option:")
    # print("1. List all authors")
    print("1. Author Menu")
    print("2. List books")
    print("3. Exit program")
   

def add_update_delete_submenu():
    while True:
        print("Select an option: ")
        print("1. List authors")
        print("2. View author details") #TODO
        print("2. Add an author")
        print("3. Delete an author")
        print("4. Update an author")
        print("5. Go back to the main menu")
        print("6. Exit the program")
        choice = input("> ")
        if choice == "1":
            space()
            list_authors()
            space()
        elif choice == "2":
            add_authors()
            space()
            print("Author added successfully.")
            space()
        elif choice == "3":
            space()
            print("Pick an author you would like to remove:")
            list_authors()
            space()
            delete_author()
            space()
        elif choice == "4":
            update_author()
        elif choice == "5":
            main()
        elif choice == "6":
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
            print("Invalid choice")
    


if __name__ == "__main__":
    main()

