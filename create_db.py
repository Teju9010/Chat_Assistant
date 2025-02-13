import sqlite3

from matplotlib.pyplot import show
conn = sqlite3.connect("company.db")
cursor =conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Salary INTEGER NOT NULL,
    Hire_Date TEXT NOT NULL

)
""")

#creating Employees table
cursor.executemany("""
INSERT INTO Employees (Name, Department, Salary, Hire_date)
VALUES (?, ?, ?, ?)
""", [
    ('Alice', 'Sales', 50000, '2021-01-15'),
    ('Bob', 'Engineering', 70000, '2020-06-10'),
    ('Charlie', 'Marketing', 60000, '2022-03-20'),
    ('David', 'Sales', 55000, '2023-02-10'),
    ('Emma', 'Engineering', 75000, '2019-08-01')
])

#creating Departments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Departments (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Manager TEXT NOT NULL
)
""")

cursor.executemany("""
INSERT INTO Departments (Name, Manager)
VALUES (?, ?)
""", [
    ('Sales', 'Alice'),
    ('Enginnering', 'Bob'),
    ('Marketing', 'Charlie'),

])

conn.commit()
conn.close()

print(" Database 'company.db' created successfully!")

