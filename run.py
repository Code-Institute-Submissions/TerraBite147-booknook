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

library = fetch_books_from_sheet()

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def prompt_choice(options):
    """Prompts user to choose from a list of options."""
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    return input("\nEnter your choice: ")


def sort_library():
    """Sorts the library by title, author, read status, or rating."""
    options = [
        "Sort by title",
        "Sort by author",
        "Sort by read status",
        "Sort by rating",
        "Return to main menu",
    ]
    choice = int(prompt_choice(options))
    sort_criteria = ["title", "author", "read", "rating"]

    if choice in [1, 2, 3, 4]:
        library.sort(key=lambda x: getattr(x, sort_criteria[choice - 1]))
        view_library(library)
    elif choice == 5:
        main_menu(library, view_library)


def add_book():
    """Adds a book to the library."""
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author of the book: ").strip()

    # Check for duplicates
    for book in library:
        if (
            book.title.lower() == title.lower()
            and book.author.lower() == author.lower()
        ):
            print(
                "\nThe book with this title and author already exists in the library."
            )
            input("\nPress enter to continue...\n")
            return

    read_status = input("Have you read this book? (yes/no): ").lower()
    read = read_status == "yes"

    while True:
        rating = input("Rate the book (1-5) or type 'skip' to skip rating: ").lower()
        if rating == "skip":
            rating = None
            break
        elif rating in ["1", "2", "3", "4", "5"]:
            rating = int(rating)
            break

    library.append(Book(title, author, read, rating))
    print(f"\n'{title}' by {author} has been added to the library!")
    input("\nPress enter to continue...\n")


def remove_book():
    """Removes a book from the library."""
    if not library:
        print("The library is empty.")
        input("\nPress enter to continue...\n")
        return

    print("Select a book to remove from the library:")
    for idx, book in enumerate(library, 1):
        print(f"{idx}. {book.title} by {book.author}")

    while True:
        try:
            choice = int(input("\nEnter the number of the book you want to remove: "))
            if 1 <= choice <= len(library):
                removed_book = library[choice - 1]
                # Confirm deletion
                confirmation = input(
                    f"Are you sure you want to remove '{removed_book.title}' by {removed_book.author}? (yes/no): "
                ).lower()
                if confirmation == "yes":
                    library.pop(choice - 1)
                    print(
                        f"\n'{removed_book.title}' by {removed_book.author} has been removed from the library!"
                    )
                    break
                elif confirmation == "no":
                    print(
                        f"\n'{removed_book.title}' by {removed_book.author} was not removed."
                    )
                    break
                else:
                    print("Invalid response. Please enter 'yes' or 'no'.")
            else:
                print(
                    f"Invalid choice. Please select a number between 1 and {len(library)}."
                )
        except ValueError:
            print("Please enter a valid number.")

    input("\nPress enter to continue...\n")


def search_for_book():
    """Searches for a book by title or author."""
    while True:
        options = ["Search by Title", "Search by Author", "Return to main menu"]
        choice = int(prompt_choice(options))

        if choice in [1, 2]:
            keyword = (
                input("Enter the title keyword: ").lower()
                if choice == 1
                else input("Enter the author keyword: ").lower()
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
                    "Enter another title/author or press 'Q' to return: "
                ).lower()
                if action == "q":
                    return

        elif choice == 3:
            return


def about_library_system():
    """Displays information about the library system."""
    clear_screen()
    print(
        "The BookNook is a Personal Library Management System that allows you to manage your personal collection of books.\n"
    )
    input("Press Enter to return to main menu\n")


library_menu_functions = [sort_library, add_book, remove_book]


def main_menu(library, view_library_fn):
    """Displays Main Menu"""
    clear_screen()
    while True:
        print("\n--- Personal Library Management System ---")
        print("1. View Library")
        print("2. Search for a Book")
        print("3. About")
        print("4. Exit")

        choice = input("Enter your choice: \n")

        if choice == "1":
            view_library_fn(library)
        elif choice == "2":
            search_for_book()
        elif choice == "3":
            about_library_system()
        elif choice == "4":
            print(
                "Exiting... Thank you for using the Personal Library Management System!"
            )
            break
        else:
            print("Invalid choice. Please try again.")


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
    print("1. Sort Library")
    print("2. Add a Book")
    print("3. Remove a Book")
    print("4. Return to main menu")

    choice = int(input("\nEnter your choice: \n")) - 1
    if 0 <= choice < len(library_menu_functions):
        library_menu_functions[choice]()
    elif choice == 3:
        return
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main_menu(library, view_library)
