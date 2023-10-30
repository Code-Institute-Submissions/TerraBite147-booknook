# imports
from tabulate import tabulate
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# Google Sheets connection
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("booknook-library").sheet1

def clear_screen():
    """Clear the terminal screen."""
    os.system("clear")

def display_options_in_columns(options):
    """Displays menu options in two columns."""
    
    # Split the options into two columns
    half_length = len(options) // 2
    col1 = options[:half_length]
    col2 = options[half_length:]
    
    # Calculate the maximum length of options in the first column
    max_length_col1 = max(len(option) for option in col1)

    # Display each pair of options side-by-side
    for i in range(half_length):
        # If there's an option in the second column to pair with the first column option
        if i < len(col2):
            print(f"{i+1}. {col1[i].ljust(max_length_col1 + 5)} {i+half_length+1}. {col2[i]}")
        else:
            print(f"{i+1}. {col1[i]}")


def fetch_books_from_sheet():
    """Fetch all books from Google Sheets and return as a list of Book objects."""
    rows = sheet.get_all_records()  # Returns a list of dictionaries
    books = [Book(row['Title'], row['Author'], row['Status'] == 'Read', row.get('Rating')) for row in rows]
    return books

def add_book_to_sheet(book):
    """Add a book to the Google Sheet."""
    read_status = "Read" if book.read else "Unread"
    sheet.append_row([book.title, book.author, read_status, book.rating or "Unrated"])

#classes    
# book class
class Book:
    def __init__(self, title, author, read=False, rating=None):
        self.title = title
        self.author = author
        self.read = read
        self.rating = rating

    def display(self):
        """Displays the book's title, author, read status, and rating."""
        read_status = "Read" if self.read else "Unread"
        rating = self.rating if self.rating else "Unrated"

        # Using string formatting
        return "{:<30} | {:<25} | {:<10} | {:<10}".format(
            f"Title: {self.title}",
            f"Author: {self.author}",
            f"Status: {read_status}",
            f"Rating: {rating}",
        )
#Pulls library from Google Sheets
library = fetch_books_from_sheet()

def prompt_choice(options):
    """Prompts user to choose from a list of options."""
    while True:
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        try:
            choice = int(input("\nEnter your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print(f"Please choose a number between 1 and {len(options)}.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")



def sort_books_by_criteria(criteria):
    """Sorts the books by given criteria."""
    def sort_key(item):
        value = getattr(item, criteria)
        # Treat None as a low value; adjust as required
        if value is None:
            return (0, )  # Using a tuple so you can add more sort keys if needed
        if isinstance(value, str):
            return (1, value)  # Strings come after None
        if isinstance(value, (int, float)):
            return (2, value)  # Numbers come after strings

    library.sort(key=sort_key)

def sort_library():
    """Sorts the library by title, author, read status, or rating."""
    if not library:
        print("Your library is empty.")
        return

    options = [
        "Sort by title",
        "Sort by author",
        "Sort by read status",
        "Sort by rating",
        "Return to main menu"
    ]

    display_options_in_columns(options)
    
    while True:
        try:
            choice = input("\nEnter your choice: ")
            choice = int(choice)

            if choice not in range(1, len(options) + 1):
                raise ValueError

            break
        except ValueError:
            print("Invalid choice. Please enter a number from the options.")
            
    sort_criteria = ["title", "author", "read", "rating"]

    if choice in [1, 2, 3, 4]:
        sort_books_by_criteria(sort_criteria[choice - 1])
        view_library(library)
    elif choice == 5:
        main_menu(library, view_library)


def get_book_details():
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author of the book: ").strip()
    return title, author

def check_duplicate_book(title, author):
    for book in library:
        if book.title.lower() == title.lower() and book.author.lower() == author.lower():
            return True
    return False

def get_read_status():
    read_status = input("Have you read this book? (yes/no): ").lower()
    if read_status not in ["yes", "no"]:
        raise ValueError("Invalid response. Please enter 'yes' or 'no'.")
    return read_status == "yes"

def get_book_rating():
    while True:
        rating = input("Rate the book (1-5) or type 'skip' to skip rating: ").lower()
        if rating == "skip":
            return None
        elif rating in ["1", "2", "3", "4", "5"]:
            return int(rating)
        else:
            print("Invalid rating. Please choose between 1-5 or type 'skip'.")

def add_book():
    """Adds a book to the library."""
    try:
        title, author = get_book_details()

        # Check for duplicates
        if check_duplicate_book(title, author):
            print("\nThe book with this title and author already exists in the library.")
            input("\nPress enter to continue...\n")
            return

        read = get_read_status()
        rating = get_book_rating()

        # Create a Book object and add to the library
        new_book = Book(title, author, read, rating)
        library.append(new_book)

        # Add the book to the Google Sheet
        add_book_to_sheet(new_book)

        print(f"\n'{title}' by {author} has been added to the library!")
        input("\nPress enter to continue...\n")

    except ValueError as e:
        print(f"Error: {e}")
        input("\nPress enter to continue...\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        input("\nPress enter to continue...\n")


def remove_book():
    """Removes a book from the library."""
    if not library:
        print("The library is empty.")
        input("\nPress enter to continue...\n")
        return

    # If there are more than 10 books, display them in columns
    if len(library) > 10:
        book_options = [f"{book.title} by {book.author}" for book in library]
        display_options_in_columns(book_options)
    else:
        for idx, book in enumerate(library, 1):
            print(f"{idx}. {book.title} by {book.author}")

    while True:
        try:
            choice = int(input("\nEnter the number of the book you want to remove: \n"))
            if 1 <= choice <= len(library):
                removed_book = library[choice - 1]
                break
            else:
                print(f"Please select a number between 1 and {len(library)}.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        confirmation = input(
            f"\nAre you sure you want to remove '{removed_book.title}' by {removed_book.author}? (yes/no): \n"
        ).lower()
        if confirmation == "yes":
            library.pop(choice - 1)
            print(f"'{removed_book.title}' by {removed_book.author} has been removed from the library!")
            break
        elif confirmation == "no":
            print(f"'{removed_book.title}' by {removed_book.author} was not removed.")
            break
        else:
            print("Please respond with 'yes' or 'no'.")

    input("\nPress enter to continue...\n")


def search_for_book():
    """Searches for a book by title or author."""
    while True:
        options = ["Search by Title", "Search by Author", "Return to main menu"]
        
        print("\n--- Search Menu ---")
        display_options_in_columns(options)
        choice = int(input("\nEnter your choice: \n"))

        if choice in [1, 2]:
            keyword = (
                input("Enter the title keyword: \n").lower()
                if choice == 1
                else input("Enter the author keyword: \n").lower()
            )
            matches = [
                book
                for book in library
                if keyword
                in getattr(book, "title" if choice == 1 else "author").lower()
            ]

            clear_screen()
            if matches:
                for book in matches:
                    print(book.display())
                input("\nPress enter to continue...\n")
                return
            else:
                action = input(
                    "Enter another title/author or press 'Q' to return: \n"
                ).lower()
                if action == "q":
                    return

        elif choice == 3:
            return



def about_booknook():
    """Displays information about the library system."""
    clear_screen()
    print("Welcome to BookNook: Your Personal Library Management System!")
    print("-" * 80)  # prints a divider line
    
    print(
        "\nBookNook is designed to help you manage and keep track of your personal collection of books."
        "\nWith BookNook, you can:"
        "\n\n1. Manage your book collection."
        "\n2. View your entire library."
        "\n3. Record if you've read a book and rate it on a scale of 1-5."
        "\n4. Integrated with Google Sheets to ensure BookNook is portable."
        "\n5. Easily search, update, add or remove books from your collection."
        "\n\nOur system is user-friendly and aims to make your reading journey more organized and enjoyable!"
    )
    
    print("\nTechnical Details:")
    print("- Developed in Python with a focus on user experience.")
    print("- Utilizes object-oriented programming principles.")
    print("- Integration capability with Google Sheets using relevant APIs.")
    
    print("\nWe continuously aim to improve BookNook. Your feedback is valuable!")
    
    input("\nPress Enter to return to the main menu.")


library_menu_functions = [sort_library, add_book, remove_book]


def main_menu(library, view_library_fn):
    """Displays Main Menu"""
    clear_screen()
    while True:
        print("\n--- Personal Library Management System ---")

        options = [
            "View Library",
            "Search for a Book",
            "About",
            "Exit"
        ]

        display_options_in_columns(options)
        
        try:
            choice = int(input("\nEnter your choice: \n"))

            if choice == 1:
                view_library_fn(library)
            elif choice == 2:
                search_for_book()
            elif choice == 3:
                about_booknook()
            elif choice == 4:
                print(
                    "Exiting... Thank you for using the Personal Library Management System!"
                )
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number corresponding to the options.")



def view_library(library):
    """Displays all books in the library and provides library options."""
    clear_screen()

    if not library:
        print("Your library is empty!")
    else:
        # Prepare data for tabulate
        table_data = []
        headers = ["Title", "Author", "Status", "Rating"]

        for book in library:
            read_status = "Read" if book.read else "Unread"
            rating = book.rating if book.rating else "Unrated"
            table_data.append([book.title, book.author, read_status, rating])

        # Use tabulate to print the data
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    print("\n--- Library Menu ---")
    options = [
        "Sort Library",
        "Add a Book",
        "Remove a Book",
        "Return to main menu"
    ]
    display_options_in_columns(options)

    choice = int(input("\nEnter your choice: \n")) - 1
    if 0 <= choice < len(library_menu_functions):
        library_menu_functions[choice]()
    elif choice == 3:
        return
    else:
        print("Invalid choice!")



if __name__ == "__main__":
    main_menu(library, view_library)
