# english_sql_mysql.py

import google.generativeai as genai
import mysql.connector
import re
import os

# ====== API Key (from environment, hidden) ======
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY") # ENTER YOUR SPECIFIED AI MODEL API KEY 
genai.configure(api_key=API_KEY)

# ====== User Inputs for DB Connection ======
DB_HOST = input("Enter MySQL Host : ") or "localhost" 
DB_USER = input("Enter MySQL Username : ") or "root"
DB_PASSWORD = input("Enter MySQL Password : ") or "root"
DB_NAME = input("Enter Database Name : ") or "test_db"

# ====== Connect to MySQL ======
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = conn.cursor()

# ====== Fetch Table Schema ======
def get_table_schema(cursor, table_name):
    cursor.execute(f"DESCRIBE {table_name}")
    columns = cursor.fetchall()
    
    schema_text = f"Table: {table_name}\nColumns:\n"
    for col in columns:
        schema_text += f"  {col[0]} {col[1]}\n"
    return schema_text

# ====== English → SQL ======
def english_to_sql(english_prompt, table_schema):
    prompt = f"""
    You are an SQL expert.
    Convert the following English request into a valid MySQL query.
    Do NOT include any code fences like ```sql``` or ```mysql```.
    Only return the pure SQL statement.

    Schema:
    {table_schema}

    English request:
    {english_prompt}
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    sql = response.text.strip()
    sql = re.sub(r"```.*?```", "", sql, flags=re.DOTALL).strip()
    return sql

# ====== Main Program ======
table_name = input("Enter table name : ")
schema = get_table_schema(cursor, table_name)
#print("\nDetected Schema:\n", schema)

while True:
    english_text = input("\nAsk your question in English (or type 'exit' to quit): ")
    if english_text.lower() == "q":
        break
    
    try:
        sql_query = english_to_sql(english_text, schema)
        print("\nGenerated SQL Query:\n", sql_query)

        cursor.execute(sql_query)
        results = cursor.fetchall()
        
        if results:
            print("\nQuery Results:")
            for row in results:
                print(row)
        else:
            print("\nNo results found.")
    except Exception as e:
        print("Error:", e)

# ====== Close ======
conn.close()
