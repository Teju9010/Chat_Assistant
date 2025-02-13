
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
from datetime import datetime

class ActionListEmployees(Action):
    def name(self):
        return "action_list_employees"
        print(f" Extracted department: {department}")

    def run(self, dispatcher: CollectingDispatcher , tracker: Tracker, domain):
        department = tracker.get_slot("department")
        
        if not department:
            dispatcher.utter_message(text=" Please specify a department (e.g., Sales, Engineering).")
            return []
        conn = sqlite3.connect("company.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Name FROM Employees WHERE Department = ?", (department,))
        employees = cursor.fetchall()
        conn.close()

        if employees:
            response = f"Employees in {department}: " + ", ".join(emp[0] for emp in employees)
        else:
            response = f"No employees found in {department}. Please check the department name"

        dispatcher.utter_message(text=response)
        return []

class ActionDepartmentManager(Action):
    def name(self):
        return "action_department_manager"

    def run(self, dispatcher, tracker, domain):
        department = tracker.get_slot("department")
        
        if not department:
            dispatcher.utter_message(text="Please specify a department (e.g., Sales, Engineering).")
            return []
        conn = sqlite3.connect("company.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Manager FROM Departments WHERE Name = ?", (department,))
        manager = cursor.fetchone()
        conn.close()

        if manager:
            response = f"The manager of {department} is {manager[0]}."
        else:
            response = f"No manager found for {department}. Please check the department name."

        dispatcher.utter_message(text=response)
        return []

class ActionEmployeesHiredAfter(Action):
    def name(self):
        return "action_employees_hired_after"

    def run(self, dispatcher, tracker, domain):
        hire_date = tracker.get_slot("date")
        
        if not hire_date:
            dispatcher.utter_message(text=" Please provide a valid date (e.g., 2022-01-01).")
            return []

        
        try:
            datetime.strptime(hire_date, "%Y-%m-%d")
        except ValueError:
            dispatcher.utter_message(text="Invalid date format. Use YYYY-MM-DD.")
            return []
        
        conn = sqlite3.connect("company.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Name FROM Employees WHERE Hire_Date > ?", (hire_date,))
        employees = cursor.fetchall()
        conn.close()

        if employees:
            response = "Employees hired after {}: ".format(hire_date) + ", ".join(emp[0] for emp in employees)
        else:
            response = f"No employees found hired after {hire_date}."

        dispatcher.utter_message(text=response)
        return []

class ActionTotalSalaryExpense(Action):
    def name(self):
        return "action_total_salary_expense"

    def run(self, dispatcher, tracker, domain):
        department = tracker.get_slot("department")
        
        if not department:
            dispatcher.utter_message(text="Please specify a department (e.g., Sales, Engineering).")
            return []
        
        conn = sqlite3.connect("company.db")
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(Salary) FROM Employees WHERE Department = ?", (department,))
        total_salary_expense = cursor.fetchone()
        conn.close()

        if total_salary_expense and total_salary_expense[0]:
            response = f"The total salary expense for {department} is Rs.{total_salary_expense[0]}."
        else:
            response = f"No salary data found for {department}. Please check the department name."

        dispatcher.utter_message(text=response)
        return []


