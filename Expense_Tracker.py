import json
import os
from datetime import datetime

# Define file path for storing expense data
DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        return {"expenses": [], "categories": []}

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file)

def input_expense(categories):
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter the category (or type 'new' to add a new category): ").lower()
    if category == 'new':
        category = input("Enter the new category: ").lower()
        categories.append(category)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"amount": amount, "description": description, "category": category, "date": date}

def categorize_expenses(expenses):
    categories = {}
    for expense in expenses["expenses"]:
        category = expense["category"]
        if category not in categories:
            categories[category] = 0
        categories[category] += expense["amount"]
    return categories

def monthly_summary(expenses):
    current_month = datetime.now().strftime("%Y-%m")
    monthly_total = sum(expense["amount"] for expense in expenses["expenses"] if expense["date"].startswith(current_month))
    return monthly_total

def main():
    expenses_data = load_expenses()
    expenses = expenses_data["expenses"]
    categories = expenses_data["categories"]

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Expenditure")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            expense = input_expense(categories)
            expenses.append(expense)
            save_expenses({"expenses": expenses, "categories": categories})
            print("Expense added successfully.")
        elif choice == "2":
            print("Monthly Summary:", monthly_summary(expenses_data))
        elif choice == "3":
            print("Category-wise Expenditure:", categorize_expenses(expenses_data))
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
