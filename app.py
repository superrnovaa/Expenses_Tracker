from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Expense

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db.init_app(app)

@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([{'id': e.id, 'name': e.name, 'amount': e.amount, 'category':e.category, 'timestamp': e.timestamp} for e in expenses])

@app.route('/api/expenses', methods=['POST'])
def add_expense_api():
    data = request.json
    new_expense = Expense(
        name=data['name'],
        amount=data['amount'],
        category=data['category'], 
        timestamp=data.get('timestamp')  # Optional: Use provided timestamp or default
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'id': new_expense.id, 'name': new_expense.name, 'amount': new_expense.amount, 'category': new_expense.category, 'timestamp': new_expense.timestamp}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)