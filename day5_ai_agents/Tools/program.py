# API Tools
import requests

city = "Delhi"

url = f"https://api.weatherapi.com/v1/current.json?key=API_KEY&q={city}"

response = requests.get(url)

data = response.json()

print("Temperature:", data["current"]["temp_c"])


# Database Tools
import sqlite3

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("INSERT INTO users (name) VALUES (?)", ("Jabir",))

conn.commit()

cursor.execute("SELECT * FROM users")

print(cursor.fetchall())

conn.close()



# File Tools

with open("notes.txt", "r") as file:
    content = file.read()

print(content)


# Python Execution Tools
numbers = [10, 20, 30]

total = sum(numbers)

print("Total:", total)


# Email Tools
import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login("your_email@gmail.com", "password")

message = "Hello from AI Agent"

server.sendmail(
    "your_email@gmail.com",
    "receiver@gmail.com",
    message
)

server.quit()


# Custom Tool Example
from langchain.tools import tool

@tool
def check_attendance(employee_id: str):
    """
    Check employee attendance status.
    """

    database = {
        "EMP101": "Present",
        "EMP102": "Absent"
    }

    return database.get(employee_id, "Not Found")

result = check_attendance.invoke({
    "employee_id": "EMP101"
})

print(result)
