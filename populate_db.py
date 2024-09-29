from datetime import datetime, timedelta
import random
from models import db, Expense  # Ensure you import your models
from app import app  # Import your Flask app

# Categories for the expenses
categories = [
    'Food & Drinks',
    'Bills & Payments',
    'Entertainment',
    'Shopping',
    'Transportation',
    'Other'
]

# Function to generate dummy expenses
def generate_dummy_expenses():
    today = datetime.utcnow()
    expenses = []
    
    # Generate expenses for the last 3 months
    for i in range(90):  # 90 days
        expense_date = today - timedelta(days=i)
        expense = Expense(
            name=f"Dummy Expense {i + 1}",
            amount=round(random.uniform(5, 100), 2),  # Random amount between 5 and 100
            category=random.choice(categories),
            timestamp=expense_date
        )
        expenses.append(expense)
    
    return expenses

# Main function to populate the database
def main():
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        expenses = generate_dummy_expenses()
        db.session.bulk_save_objects(expenses)  # Bulk insert expenses
        db.session.commit()  # Commit the session
        print(f"Inserted {len(expenses)} dummy expenses into the database.")

if __name__ == '__main__':
    main()
