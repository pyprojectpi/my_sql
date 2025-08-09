from flask import Flask, render_template, request, url_for
import mysql.connector

app = Flask(__name__)

def get_student_data(reg_no, dob):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sslc_db"
    )
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM students WHERE reg_no=%s AND dob=%s"
    cursor.execute(query, (reg_no, dob))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    reg_no = request.form['regno']
    dob = request.form['dob']  # dd/mm/yyyy

    try:
        dob_parts = dob.split('/')
        formatted_dob = f"{dob_parts[2]}-{dob_parts[1]}-{dob_parts[0]}"
    except:
        return "Invalid date format. Use dd/mm/yyyy"

    student = get_student_data(reg_no, formatted_dob)
    if student:
        return render_template("result.html", student=student)
    else:
        return "No record found. Please check your details."

if __name__ == '__main__':
    app.run(debug=True)
