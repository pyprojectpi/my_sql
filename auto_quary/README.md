# 🗣️ English-to-SQL Converter (MySQL + Google Gemini AI)

This project converts **natural language (English)** queries into **SQL queries** and executes them on a MySQL database.  
It uses **Google Gemini AI** for SQL generation and Python's `mysql-connector-python` for database connectivity.

---

## 🚀 Features
- Convert **plain English** into **valid MySQL queries**
- Automatically execute queries and fetch results
- Display **database schema** dynamically
- Securely store API keys using `.env`
- User-friendly CLI

---

## 🛠️ Tech Stack
- **Python 3.8+**
- **Google Gemini API**
- **MySQL**
- **mysql-connector-python**
- **dotenv**

---

## 📂 Project Structure
english-to-sql-mysql/
│-- main.py # Main application script
│-- requirements.txt # Python dependencies
│-- .env # API keys & database credentials (not uploaded to GitHub)
│-- .gitignore # Ignore sensitive files
│-- README.md # Project documentation


---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/english-to-sql-mysql.git
cd english-to-sql-mysql
pip install -r requirements.txt

Enter your question: Show all employees in the IT department
Generated SQL: SELECT * FROM employees WHERE department = 'IT';
Results:
+----+---------------+------------+--------+
| id | name          | department | salary |
+----+---------------+------------+--------+
|  1 | Alice Johnson | IT         |  75000 |
|  4 | Diana Prince  | IT         |  82000 |
|  8 | Hannah Lee    | IT         |  91000 |
+----+---------------+------------+--------+
