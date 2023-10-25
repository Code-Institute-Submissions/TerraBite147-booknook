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
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    return input("\nEnter your choice: ")


def view_library():
    clear_screen()
    if not library:
        print("The library is empty.")
    else:
        for book in library:
            print(book.display())

    options = ["Sort", "Add", "Remove", "Return to main menu"]
    choice = int(prompt_choice(options))
    library_menu_functions[choice - 1]()


def sort_library():
    options = ["Sort by title", "Sort by author", "Sort by read status", "Sort by rating", "Return to main menu"]
    choice = int(prompt_choice(options))
    sort_criteria = ["title", "author", "read", "rating"]

    if choice in [1, 2, 3, 4]:
        library.sort(key=lambda x: getattr(x, sort_criteria[choice - 1]))
        view_library()
    elif choice == 5:
        main_menu()


def add_book():
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
    title = input("Enter the title of the book you want to remove: ").strip()
    book_to_remove = next((book for book in library if book.title.lower() == title.lower()), None)

    if book_to_remove:
        library.remove(book_to_remove)
        print(f"\n'{title}' has been removed from the library!")
    else:
        print(f"\nBook titled '{title}' is not found in the library.")

    input("\nPress enter to continue...\n")


def search_for_book():
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


library_menu_functions = [sort_library, add_book, remove_book, main_menu]


def about_library_system():
    clear_screen()
    print("The BookNook is a Personal Library Management System that allows you to manage your personal collection of books.")
    options = ["Return to main menu"]
    prompt_choice(options)


def main_menu():
    while True:
        clear_screen()
        print("--- Personal Library Management System ---")
        options = ["View Library", "Search for a Book", "About", "Exit"]
        choice = int(prompt_choice(options))

        if choice == 1:
            view_library()
        elif choice == 2:
            search_for_book()
        elif choice == 3:
            about_library_system()
        elif choice == 4:
            print("\nExiting... Thank you for using the Personal Library Management System!")
            break


if __name__ == "__main__":
    main_menu()






