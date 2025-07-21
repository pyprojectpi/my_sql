# 🛒 Online Retail Store – SQL Project

This project simulates a real-world **e-commerce database** similar to platforms like Amazon, Flipkart, or Meesho. It manages customer orders, products, payments, and reviews using a relational database model.

---

## 📁 Project Structure

- `create_tables.sql` – SQL script to create all tables.
- `insert_data.sql` – SQL script to insert sample data.
- `queries.sql` – Sample business queries.
- `ER_diagram.png` – Entity Relationship diagram of the database.
- `README.md` – Project documentation.

---

## 🎯 Objectives

- Design a normalized relational database for an e-commerce store.
- Write SQL queries for real-world use cases.
- Demonstrate JOINs, GROUP BY, aggregate functions, and subqueries.
- Understand how transactions like orders and payments are tracked in retail.

---

## 🧱 Database Schema

### Tables:
- **Customers** – Stores customer details.
- **Products** – Product catalog.
- **Orders** – Orders placed by customers.
- **Order_Items** – Line items of each order.
- **Payments** – Payment information for each order.
- **Reviews** – Product ratings and feedback.

---

## 💻 Key SQL Features Used

- `JOIN` operations
- `GROUP BY`, `ORDER BY`
- Aggregations (`SUM`, `AVG`, `COUNT`)
- Foreign Key constraints
- Subqueries

---

## 🔍 Sample Queries

- List all orders with customer and product details
- Calculate total revenue from paid orders
- Top 3 best-selling products
- Average rating per product
- Customers with pending payments

---

## 📸 ER Diagram

> Refer to the `ER_diagram.png` file for a visual overview of the database structure.

---

## 🚀 How to Run

1. Open **MySQL Workbench** / **phpMyAdmin** / **SQLite**.
2. Execute `create_tables.sql`.
3. Run `insert_data.sql` to populate with sample data.
4. Use `queries.sql` to test functionality.

---

## 🧠 Future Improvements

- Add triggers for stock update
- Integrate with a web UI using Flask or PHP
- Add product categories and discounts
- Normalize address and payment methods further

---

## 📞 Contact

For queries or collaboration:  
**Name: surya  
**Email: suryaarumugam2021@gmail.com
**Portfolio: https://thunderous-cascaron-dc8b57.netlify.app/

---

