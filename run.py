# imports 
import os


class Book:
    def __init__(self, title, author, read=False, rating=None):
        self.title = title
        self.author = author
        self.read = read
        self.rating = rating

    def display(self):
        read_status = "Read" if self.read else "Unread"
        rating = self.rating if self.rating else "Unrated"
        return f"Title: {self.title}, Author: {self.author}, Status: {read_status}, Rating: {rating}"


library = [
    Book("Pride and Prejudice", "Jane Austen"),
    Book("To Kill a Mockingbird", "Harper Lee", True, 5),
    Book("The Great Gatsby", "F. Scott Fitzgerald"),
]


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
    options = ["Sort by title", "Sort by author", "Sort by read status", "Sort by rating", "Return to main menu"]
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
        if book.title.lower() == title.lower() and book.author.lower() == author.lower():
            print("\nThe book with this title and author already exists in the library.")
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
    title = input("Enter the title of the book you want to remove: ").strip()
    book_to_remove = next((book for book in library if book.title.lower() == title.lower()), None)

    if book_to_remove:
        library.remove(book_to_remove)
        print(f"\n'{title}' has been removed from the library!")
    else:
        print(f"\nBook titled '{title}' is not found in the library.")

    input("\nPress enter to continue...\n")


def search_for_book():
    """Searches for a book by title or author."""
    while True:
        options = ["Search by Title", "Search by Author", "Return to main menu"]
        choice = int(prompt_choice(options))

        if choice in [1, 2]:
            keyword = input("Enter the title keyword: ").lower() if choice == 1 else input("Enter the author keyword: ").lower()
            matches = [book for book in library if keyword in getattr(book, "title" if choice == 1 else "author").lower()]

            clear_screen()
            if matches:
                for book in matches:
                    print(book.display())
                input("\nPress enter to continue...\n")
                return
            else:
                action = input("Enter another title/author or press 'Q' to return: ").lower()
                if action == 'q':
                    return

        elif choice == 3:
            return


library_menu_functions = [sort_library, add_book, remove_book]


def about_library_system():
    """Displays information about the library system."""
    clear_screen()
    print("The BookNook is a Personal Library Management System that allows you to manage your personal collection of books.")
    options = ["Return to main menu"]
    prompt_choice(options)


def main_menu(library, view_library_fn):
    """Displays Main Menu"""
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
        for book in library:
            print(book.display())
    
    print("\n--- Library Menu ---")
    print("1. Sort Library")
    print("2. Add a Book")
    print("3. Remove a Book")
    print("4. Return to main menu")
    
    choice = int(input("\nEnter your choice: \n")) - 1 # Subtract 1 for 0-based index
    if 0 <= choice < len(library_menu_functions):
        library_menu_functions[choice]()
    elif choice == 3:  # Corresponds to "4. Return to main menu" option
        main_menu(library, view_library)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main_menu(library, view_library)






