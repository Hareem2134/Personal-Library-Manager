# **📚 Personal Library Manager**  

## **📌 Overview**  
**Personal Library Manager** is a **versatile book management tool** available in **two versions**:  

🔹 **CLI Version (`library_manager_cli.py`)** – A **command-line app** to **add, remove, search, and track books**, ensuring **persistent storage in `library.txt`**.  

🔹 **Streamlit Version (`library_manager_streamlit.py`)** – A **web-based app** with a **modern UI**, allowing users to manage their library **online**, with data stored in **`library.json`**.  

Both versions **store book data automatically**, ensuring your collection is always saved. 🚀  

---

## **🚀 Features**  

✅ **Add Books** – Enter title, author, publication year, genre & read status.  
✅ **Remove Books** – Delete books from the library using their title.  
✅ **Search Books** – Find books by title or author.  
✅ **Display All Books** – View a formatted list of stored books.  
✅ **Statistics** – Get insights on total books & percentage read.  
✅ **Persistent Storage** – Books are **saved & loaded automatically** (`library.txt` for CLI, `library.json` for Streamlit).  
✅ **User-Friendly** – Available in **CLI and Streamlit UI** versions.  

---

## **🛠️ Installation**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Hareem2134/Personal-Library-Manager
cd personal-library-manager
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

---

## **📖 How to Use**  

### **📌 CLI Version (`library_manager_cli.py`)**  
Run the command-line version:  
```bash
python library_manager_cli.py
```
📁 **Books are stored in `library.txt` automatically.**  

---

### **📌 Streamlit Web App (`library_manager_streamlit.py`)**  
Run the web-based version:  
```bash
streamlit run library_manager_streamlit.py
```
📁 **Books are stored in `library.json` automatically.**  

🔗 **[Try the Live App](https://personal-library-manager-by-hareemfarooqi.streamlit.app/)**  

---

## **📥 File Handling**  

📁 **CLI Version** – Books are stored in `library.txt`.  
📁 **Streamlit Version** – Books are stored in `library.json`.  
🔄 **Data is automatically saved & loaded** when the program starts.  

---

## **🛡️ Privacy & Security**  

🔒 **No data is transmitted online** – everything is stored **locally**.  
🚫 **No tracking, analytics, or advertisements**.  
🛠️ **Your personal book collection remains private**.  

---

## **📞 Contact**  

For queries, feedback, or collaboration, connect with me:  

- **LinkedIn** 🔗 [Hareem Farooqi](https://www.linkedin.com/in/hareemfarooqi/)  
- **Email** 📧 hareemfarooqi2134@gmail.com  

---

## **🚀 Future Improvements**  

💡 **Enhance UI with more customization in Streamlit**.  
💡 **Enable sorting** by **title, author, or publication year**.  
💡 **Export book data** to a **CSV file** for easy sharing.  
💡 **Implement a backup system** to prevent accidental data loss.