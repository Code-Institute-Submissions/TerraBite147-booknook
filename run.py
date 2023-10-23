# imports
import os


# Data structure for the library
library = [
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "read": True,
        "rating": 5,
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "read": False,
        "rating": None,
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
            view_library()
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

def view_library():
    clear_screen()
    """Displays the library"""
    print("\n--- Library ---")
    if len(library) == 0:
        print("The library is empty.")
    else:
        for book in library:
            read_status = "Read" if book['read'] else "Unread"
            rating = book['rating'] if book['rating'] else "Unrated"
            print(f"Title: {book['title']}, Author: {book['author']}, Status: {read_status}, Rating: {rating}\n")
    input("Press enter to return to main menu.\n")

    # Options after displaying the library
    print("\nOptions:")
    print("1. Sort")
    print("2. Add")
    print("3. Remove")
    print("4. Return to main menu")        
                  

def search_for_book():
    #placehholder 
    print("\n--- Search for a Book ---")



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