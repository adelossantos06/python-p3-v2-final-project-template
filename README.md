# Library CLI

This is a Command Line Interface (CLI) application for managing authors and their books. It allows users to perform various operations such as adding, updating, deleting and viewing authors and their books. 

## Features

- Add, update, delete, and list authors.
- Add, update, delete, and list books by authors.
- View details of a specific author and their books.

## Main Menu

1. **Author Menu:** Navigate to the author managment menu
2. **Book Menu:** Navigate to the book managment menu
3. **Exit program:** Exit the application 

## Author Menu

1. **List authors:** Display all authors.
2. **View author details:** Select an author to view their details.
3. **Add an author:** Add a new author. 
4. **Delete an author:** Delete an existing author. 
5. **Update an author:** Update details of an existing author.
6. **Go back to the main menu:** Return to the main menu.
7. **Exit program:** Exit the application.
 

## Book Menu

1. **List all books:** Display all books.
2. **Add a book:** Add a new book.
3. **Update a book:** Update details of an existing book.
4. **Delete a book:** Delete an existing book.
5. **Go back to the main menu:** Return to the main menu.
6. **Exit program:** Exit the application.

## Code Organization

### lib/cli.py
This file contains the main entry point for the CLI applications and handles user interaction.

### helpers.py
This file contains helper functions for perforing operations related to authors and their books.

### models
This folder contains the models for 'Author' and 'Book' and contains the backened needed for the application. 

