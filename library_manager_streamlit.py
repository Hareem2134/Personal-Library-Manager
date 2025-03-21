import streamlit as st
import json
import os

# File to store library data
LIBRARY_FILE = "library.json"

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
        st.error("⚠ Error loading library file. The file may be corrupted. Starting with an empty library.")
        return []

# Save the library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)  # Save in readable JSON format

# Initialize session state for library data
if "library" not in st.session_state:
    st.session_state.library = load_library()

# Streamlit App UI
st.set_page_config(page_title="📚 Personal Library Manager", page_icon="📖", layout="wide")

st.title("📚 Personal Library Manager")
st.markdown("Manage your personal book collection **easily** with this interactive app! 🚀")

# Sidebar Navigation
menu = st.sidebar.radio("📌 Menu", ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Statistics"])

# Add a Book
if menu == "Add a Book":
    st.subheader("➕ Add a New Book")
    
    # Initialize session state variables for inputs
    if "title" not in st.session_state:
        st.session_state.title = ""
    if "author" not in st.session_state:
        st.session_state.author = ""
    if "year" not in st.session_state:
        st.session_state.year = 2000
    if "genre" not in st.session_state:
        st.session_state.genre = ""
    if "read" not in st.session_state:
        st.session_state.read = False

    # Input Fields
    title = st.text_input("Enter the book title", value=st.session_state.title, key="title_input")
    author = st.text_input("Enter the author", value=st.session_state.author, key="author_input")
    year = st.number_input("Enter the publication year", min_value=1000, max_value=2100, step=1, value=st.session_state.year, key="year_input")
    genre = st.text_input("Enter the genre", value=st.session_state.genre, key="genre_input")
    read = st.checkbox("Mark as Read", value=st.session_state.read, key="read_input")

    if st.button("Add Book"):
        if title and author and genre:
            new_book = {"title": title, "author": author, "year": year, "genre": genre, "read": read}
            st.session_state.library.append(new_book)
            save_library(st.session_state.library)  # Save immediately
            st.success(f"✅ '{title}' added successfully!")

            # Clear input fields after adding
            st.session_state.title = ""
            st.session_state.author = ""
            st.session_state.year = 2000
            st.session_state.genre = ""
            st.session_state.read = False

            # Rerun the script to reset fields
            st.rerun()
        else:
            st.error("⚠ Please fill in all fields!")

# Remove a Book
if menu == "Remove a Book":
    st.subheader("🗑 Remove a Book")
    book_titles = [book["title"] for book in st.session_state.library]
    book_to_remove = st.selectbox("Select the book to remove", [""] + book_titles)

    if st.button("Remove Book"):
        if book_to_remove:
            st.session_state.library = [book for book in st.session_state.library if book["title"] != book_to_remove]
            save_library(st.session_state.library)
            st.success(f"❌ '{book_to_remove}' removed successfully!")
            st.rerun()
        else:
            st.error("⚠ Please select a book to remove!")

# Search for a Book
if menu == "Search for a Book":
    st.subheader("🔍 Search for a Book")
    search_by = st.radio("Search by:", ["Title", "Author"])
    keyword = st.text_input("Enter your search keyword")

    if st.button("Search"):
        results = [
            book for book in st.session_state.library
            if keyword.lower() in book[search_by.lower()].lower()
        ]
        if results:
            st.success(f"✅ Found {len(results)} matching books:")
            for book in results:
                status = "✅ Read" if book["read"] else "❌ Unread"
                st.markdown(f"**📖 {book['title']}** by {book['author']} ({book['year']}) - *{book['genre']}* - {status}")
        else:
            st.warning("⚠ No matching books found!")

# Display All Books
if menu == "Display All Books":
    st.subheader("📖 Your Library Collection")
    if st.session_state.library:
        for book in st.session_state.library:
            status = "✅ Read" if book["read"] else "❌ Unread"
            st.markdown(f"**📖 {book['title']}** by {book['author']} ({book['year']}) - *{book['genre']}* - {status}")
    else:
        st.warning("📭 Your library is empty!")

# Statistics
if menu == "Statistics":
    st.subheader("📊 Library Statistics")
    total_books = len(st.session_state.library)
    read_books = sum(1 for book in st.session_state.library if book["read"])
    unread_books = total_books - read_books
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    st.metric("📚 Total Books", total_books)
    st.metric("✅ Books Read", read_books)
    st.metric("📖 Books Unread", unread_books)
    st.metric("📊 Reading Progress", f"{percentage_read:.2f}%")

# Footer
st.markdown("---")
st.markdown(
    "Made with ❤️ by **[Hareem Farooqi](https://www.linkedin.com/in/hareemfarooqi/)**"
)