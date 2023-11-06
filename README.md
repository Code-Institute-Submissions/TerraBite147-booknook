# BookNook Library Management System
BookNook is a Python-based library management system that allows users to manage their personal collection of books.
It integrates with Google Sheets to provide a portable solution for tracking books.

## Contents

- [Purpose](#purpose)
- [user experience](#user-experience)
    * [User Stories](#user-stories)
    * [Design](#design)
    * [Flowchart](#flowchart)
- [Features](#features)
    * [Existing Features](#existing-features)
        * [Main Menu](#main-menu)
            * [View Library](#view-library)
                * [Sort Library](#sort-library)
                    * [Sort by Title](#sort-by-title)
                    * [Sort by Author](#sort-by-author)
                    * [Sort by read status](#sort-by-read-status)
                    * [Sort by rating](#sort-by-rating)
                * [Add Book](#add-book)
                * [Remove Book](#remove-book)
                * [Edit Book](#edit-book)
            * [Search for a Book](#search-for-a-book)
                * [Search by Title](#search-by-title)
                * [Search by Author](#search-by-author)
            * [About](#about)
            * [Exit](#exit)
    * [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Libraries](#libraries)
    * [Tools](#tools)
- [Testing](#testing)
    * [Manual Testing](#manual-testing)
        * [Test 1: Main Menu](#test-1-main-menu)
        * [Test 2: View Library](#test-2-view-library)
        * [Test 3: Sort Library](#test-3-sort-library)
        * [Test 4: Add Book](#test-4-add-book)
        * [Test 5: Remove Book](#test-5-remove-book)
        * [Test 6: Edit Book](#test-6-edit-book)
        * [Test 7: Search for a Book](#test-7-search-for-a-book)
        * [Test 8: About](#test-8-about)
        * [Test 9: Exit](#test-9-exit)
    * [Bugs](#bugs)

- [Deployment](#deployment)

- [Credits](#credits)
    * [Content](#content)
    * [Acknowledgements](#acknowledgements) 

## Purpose
The purpose of this project is to create a library management system that allows users to manage their personal collection of books. It integrates with Google Sheets to provide a portable solution for tracking books. The user can add, edit, remove, and search for books in their library. The user can also sort their library by title, author, read status, and rating.

This program is developed to demonstrate competency in python programming and is purely for educational purposes.

## User Experience

### User Stories
This program is designed to be used by a user who wants to manage their personal collection of books. The user can add, edit, remove, and search for books in their library. The user can also sort their library by title, author, read status, and rating.

As a user, I want to be able to:
- View all the books in my library
- Add a book to my library
- Edit a book in my library
- Remove a book from my library
- Search for a book in my library
- Sort my library

### Design
The program is designed to be simple and intuitive to use. The user is presented with a main menu that allows them to navigate to the different features of the program. The user can navigate the menu by entering in the corresponding number for the menu item they want to select. The user can also exit the program by entering in the corresponding number for the exit menu item.

### Flowchart
During the planning phase of this project, a flowchart was created to help visualize the program's logic. The flowchart can be found below.

The flowchart was created using [lucidchart](https://www.lucidchart.com/) and was used as a guide to help develop the program.

![Flowchart](readme/flowchart.png)

## Features

### Existing Features
#### Main Menu
The main menu is the first screen the user sees when they run the program. It allows the user to navigate to the different features of the program.
View Library, Search for a Book, About, and Exit.

![Main Menu](readme/main-menu.png)

#### View Library
The view library feature allows the user to view all the books in their library. The user can also sort their library , add a book, remove a book, and edit a book.

All the books in the library are displayed in a table format. The table contains the following columns: index, title, author, read status, and rating.

The information is retrieved from a Google Sheet this is also where all the changes are saved.

![View Library](readme/view-library.png)

- #### Sort Library
    The sort library feature allows the user to sort their library by title, author, read status, and rating.

    - ##### Sort by Title
        The sort by title feature allows the user to sort their library by title 

    - ###### Sort by Author
        The sort by author feature allows the user to sort their library by author

    - ###### Sort by read status
        The sort by read status feature allows the user to sort their library by read status

    - ###### Sort by rating
        The sort by rating feature allows the user to sort their library by rating

- #### Add Book
    The add book feature allows the user to add a book to their library. The user is prompted to enter in the title, author, if they have read the book, and their rating of the book.

    Adding the book to the library also adds the book to the Google Sheet. 

    ![Add Book](readme/add-book.png)

- #### Remove Book
    The remove book feature allows the user to remove a book from their library. The user is prompted to enter in the index number of the book they want to remove.
    The user is then prompted to confirm if they want to remove the book.

    Removing the book from the library also removes the book from the Google Sheet.

    ![Remove Book](readme/remove-book.png)

- #### Edit Book
    The edit book feature allows the user to edit a book in their library. The user is prompted to enter in the index number of the book they want to edit.
    The user is then prompted to enter in the new title, author, if they have read the book, and their rating of the book.
    They also have the option to press enter to keep the original value.
    They are then prompted to confirm if they want to edit the book.

    All edits are saved to the Google Sheet.

    ![Edit Book](readme/edit-book.png)

#### Search for a Book
The search for a book feature allows the user to search for a book in their library. The user can search by title or author.

The search feature allows for partial matches. For example, if the user searches for "Har", the author the program will return all books that contain "Har" as the author eg. Harry, Harvey.

The user is then given the option to edit or remove the book or return to the main menu.

![Search for a Book](readme/search-book.png)

- #### Search by Title
    The search by title feature allows the user to search for a book by title.

- #### Search by Author
    The search by author feature allows the user to search for a book by author.

#### About
The about feature displays information about the program.

![About](readme/about.png)

#### Exit
The exit feature allows the user to exit the program.

### Features Left to Implement
- Add a feature to allow the user to export their library to a csv file.
- Add a feature to allow the user to import their library from a csv file.
- Add a page feature to allow the user to view their library in pages.

## Technologies Used

### Languages
- [Python](https://www.python.org/)
    - The project uses **Python** to create the program.

### Libraries
- [gspread](https://docs.gspread.org/en/latest/)
    - The project uses **gspread** to interact with Google Sheets.
- [oauth2client](https://oauth2client.readthedocs.io/en/latest/)
    - The project uses **oauth2client** to authenticate with Google Sheets.
- [Tabulate](https://pypi.org/project/tabulate/)
    - The project uses **tabulate** to display the library in a table format.
- [os](https://docs.python.org/3/library/os.html)
    - The project uses **os** to interact with the operating system.

### Tools
- [Google Sheets](https://www.google.com/sheets/about/)
    - The project uses **Google Sheets** to store the library data.
- [Lucidchart](https://www.lucidchart.com/)
    - The project uses **Lucidchart** to create the flowchart.
- [Github](https://github.com)
    - The project uses **Github** to store the project's code.
- [Heroku](https://www.heroku.com/)
    - The project uses **Heroku** to host the project.
- [Git](https://git-scm.com/)
    - The project uses **Git** for version control.
- [Visual Studio Code](https://code.visualstudio.com/)
    - The project uses **Visual Studio Code** as the IDE.

## Testing

### Manual Testing
#### Test 1: Main Menu
1. Run the program.
2. The main menu is displayed.
3. Press 1 to view the library.
4. The library is displayed.
5. Press 2 to search for a book.
6. The search for a book menu is displayed.
7. Restart the program.
8. The main menu is displayed.
9. Press 3 to view the about page.
10. The about page is displayed.
11. Press enter.
12. The main menu is displayed.
13. Press 4 to exit the program.
14. The program exits.


#### Test 2: Main Menu Error Handling
1. Run the program.
2. The main menu is displayed.
3. Press 5.
4. User gets Invalid choice. Please try again.

#### Test 3: View Library - Sort Library
1. Run the program.
2. The main menu is displayed.
3. Press 1 to view the library.
4. The library is displayed.
5. Press 1 to sort the library
6. Press 1 to sort by title.
7. The library is sorted by title.
8. Press 1 to sort the library.
9. Press 2 to sort by author.
10. The library is sorted by author.
11. Press 1 to sort the library.
12. Press 3 to sort by read status.
13. The library is sorted by read status.
14. Press 1 to sort the library.
15. Press 4 to sort by rating.
16. The library is sorted by rating.

#### Test 4: View Library - Sort Library Error Handling
1. Run the program.
2. The main menu is displayed.
3. Press 1 to view the library.
4. The library is displayed.
5. Press 1 to sort the library.
6. Press 5.
7. User gets Invalid choice. Please enter a number from the options and try again.
8. Press 0.
9. User gets Invalid choice. Please enter a number from the options and try again.
10. Press a.
11. User gets Invalid choice. Please enter a number from the options and try again.
12. Press 1 to sort by title.
13. The library is sorted by title.








