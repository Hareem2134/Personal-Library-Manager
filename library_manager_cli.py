import json
import os

# File to store library data
LIBRARY_FILE = "library.txt"

# Load the library from file (if exists)
def load_library():
    if not os.path.exists(LIBRARY_FILE):  
        return []  # Return an empty list if file does not exist

    if os.path.getsize(LIBRARY_FILE) == 0:  
        return []  # Return empty list if file is empty

    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)  # Load data from JSON format
    except json.JSONDecodeError:
        print("\n⚠ Error loading library file. The file may be corrupted. Starting with an empty library.\n")
        return []

# Save the library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)  # Save in readable JSON format

# Add a book to the library
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = input("Enter the publication year: ").strip()
    genre = input("Enter the genre: ").strip()
    read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {"title": title, "author": author, "year": year, "genre": genre, "read": read}
    library.append(book)
    save_library(library)  # Save immediately
    print(f"\n✅ '{title}' added successfully!\n")

# Remove a book from the library
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)  # Save immediately
            print(f"\n❌ '{title}' removed successfully!\n")
            return
    print("\n⚠ Book not found!\n")

# Search for a book by title or author
def search_book(library):
    print("\nSearch by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        keyword = input("Enter the book title: ").strip()
        results = [book for book in library if keyword.lower() in book["title"].lower()]
    elif choice == "2":
        keyword = input("Enter the author's name: ").strip()
        results = [book for book in library if keyword.lower() in book["author"].lower()]
    else:
        print("\n⚠ Invalid choice!\n")
        return
    
    if results:
        print("\n🔍 Matching Books:")
        for i, book in enumerate(results, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("\n⚠ No books found!\n")

# Display all books in the library
def display_books(library):
    if not library:
        print("\n📭 Your library is empty!\n")
        return
    
    print("\n📚 Your Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Display statistics
def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("\n📊 No books in the library!\n")
        return
    
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100

    print("\n📊 Library Statistics:")
    print(f"📖 Total books: {total_books}")
    print(f"✅ Books read: {read_books} ({percentage_read:.2f}%)")

# Main menu
def main():
    library = load_library()  # Load library from file

    while True:
        print("\n📚 Welcome to Your Personal Library Manager!\n")
        print("1️⃣ Add a book")
        print("2️⃣ Remove a book")
        print("3️⃣ Search for a book")
        print("4️⃣ Display all books")
        print("5️⃣ Display statistics")
        print("6️⃣ Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)  # Save before exiting
            print("\n📁 Library saved successfully. Goodbye!\n")
            break
        else:
            print("\n⚠ Invalid choice! Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()