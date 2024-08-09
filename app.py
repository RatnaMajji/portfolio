from flask import Flask, request, render_template, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ratna@817972", 
    database="contact_form"
)
cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            # Get form data
            name = request.form['name']
            email = request.form['email']
            mobile_number = request.form['mobile_number']
            subject = request.form['subject']
            message = request.form['message']

            # Insert data into MySQL database
            sql = "INSERT INTO contacts (name, email, mobile_number, subject, message) VALUES (%s, %s, %s, %s, %s)"
            values = (name, email, mobile_number, subject, message)
            cursor.execute(sql, values)
            db.commit()  # Commit the transaction

            # Return success response
            return render_template('index.html', success=True)
        except Exception as e:
            print(f"Error: {e}")  # Print the error to the console for debugging
            return render_template('index.html', error=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
