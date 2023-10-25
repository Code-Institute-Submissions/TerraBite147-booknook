# imports
import os


# Data structure for the library
library = [
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "read": False,
        "rating": None,
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "read": True,
        "rating": 5,
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "read": False,
        "rating": None,
    },
]


def clear_screen():
    """Clear the screen depending on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")


def main_menu():
    """Displays Main Menu"""
    while True:
        print("\n--- Personal Library Management System ---")
        print("1. View Library")
        print("2. Search for a Book")
        print("3. About")
        print("4. Exit")

        choice = input("Enter your choice: \n")

        if choice == "1":
            view_library(library)
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
    clear_screen()
    """Displays the library"""
    print("\n--- Library ---")
    if len(library) == 0:
        print("The library is empty.")
    else:
        for book in library:
            read_status = "Read" if book["read"] else "Unread"
            rating = book["rating"] if book["rating"] else "Unrated"
            print(
                f"Title: {book['title']}, Author: {book['author']}, Status: {read_status}, Rating: {rating}\n"
            )

    # Options after displaying the library
    print("\nOptions:")
    print("1. Sort")
    print("2. Add")
    print("3. Remove")
    print("4. Return to main menu")

    choice = input("\nEnter your choice: \n")
    if choice == "1":
        sort_options(library)
    elif choice == "2":
        add_book()
    elif choice == "3":
        remove_book()
        pass
    elif choice == "4":
        return
    else:
        print("Invalid choice!")

def sort_options(library):
    """Sorts the library"""
    print("\n--- Sort Options ---")
    print("1. Sort by title")
    print("2. Sort by author")
    print("3. Sort by read status")
    print("4. Sort by rating")
    print("5. Return to main menu")

    choice = input("\nEnter your choice: \n")
    sort_criteria = {"1": "title", "2": "author", "3": "rating", "4": "read"}

    if choice in sort_criteria:
        sorted_library = sort_library(library, sort_criteria[choice])
        # Display the sorted library again
        for book in sorted_library:
            read_status = "Read" if book["read"] else "Unread"
            rating = book["rating"] if book["rating"] else "Unrated"
            print(
                f"Title: {book['title']}, Author: {book['author']}, Status: {read_status}, Rating: {rating}"
            )
    elif choice == "5":
        return
    else:
        print("Invalid choice!")

def sort_library(library, criteria):
    """Sorts the library based on the criteria."""
    if criteria == "title":
        return sorted(library, key=lambda x: x["title"])
    elif criteria == "author":
        return sorted(library, key=lambda x: x["author"])
    elif criteria == "rating":
        return sorted(
            library, key=lambda x: (x["rating"] is None, x["rating"]), reverse=True
        )
    elif criteria == "read":
        return sorted(library, key=lambda x: not x["read"])

def search_for_book():
    """Search for a book in the library."""
    while True:
        print("\n--- Search for a Book ---")
        print("1. Search by Title")
        print("2. Search by Author")
        print("3. Return to main menu")

        choice = input("Enter your choice: \n")

        if choice == "1":
            keyword = input("Enter the title keyword: ").lower()
            matches = [book for book in library if keyword in book["title"].lower()]
        elif choice == "2":
            keyword = input("Enter the author keyword: ").lower()
            matches = [book for book in library if keyword in book["author"].lower()]
        elif choice == "3":
            return
        else:
            print("Invalid choice!")
            continue

        # Display matched books
        clear_screen()
        if matches:
            for book in matches:
                read_status = "Read" if book["read"] else "Unread"
                rating = book["rating"] if book["rating"] else "Unrated"
                print(
                    f"Title: {book['title']}, Author: {book['author']}, Status: {read_status}, Rating: {rating}"
                )
            input("\nPress enter to continue...\n")
            return
        else:
            print("No books found for the given keyword.")
            action = input("Enter another title/author or press 'Q' to return: ").lower()
            if action == 'q':
                return

def add_book():
    """Allows user to add a book to the library."""
    print("\n--- Add a Book ---")

    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author of the book: ").strip()

    # Check for duplicates
    for book in library:
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
            print("\nThe book with this title and author already exists in the library.")
            input("\nPress enter to continue...\n")
            return

    # Read status
    read_status = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_status == "yes" else False

    # Rating
    while True:
        rating = input("Rate the book (1-5) or type 'skip' to skip rating: ").strip().lower()
        if rating == "skip":
            rating = None
            break
        elif rating in ["1", "2", "3", "4", "5"]:
            rating = int(rating)
            break
        else:
            print("Invalid rating. Please enter a number between 1 and 5, or 'skip'.")

    # Add book to library
    library.append({
        "title": title,
        "author": author,
        "read": read,
        "rating": rating
    })

    print(f"\n'{title}' by {author} has been added to the library!")
    input("\nPress enter to continue...\n")

def remove_book():
    """Allows user to remove a book from the library."""
    print("\n--- Remove a Book ---")

    title = input("Enter the title of the book you want to remove: ").strip()

    # Search for the book in the library
    book_to_remove = next((book for book in library if book["title"].lower() == title.lower()), None)

    if book_to_remove:
        library.remove(book_to_remove)
        print(f"\n'{title}' has been removed from the library!")
    else:
        print(f"\nBook titled '{title}' is not found in the library.")

    input("\nPress enter to continue...\n")

def about_library_system():
    """About the library system."""
    clear_screen()
    print("\n--- About ---")
    print(
        "The BookNook is a Personal Library Management System allows you to manage your "
        "personal collection of books. With this system, you can:"
    )
    print("  - View your entire library")
    print("  - Search for specific books")
    print("  - Add or remove books")
    print("  - Rate them")
    print("  - Mark them as read")
    print("Stay organized and keep track of your reading with ease!")
    input("Press enter to return to main menu.\n")




if __name__ == "__main__":
    main_menu()
