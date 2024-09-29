from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField, DateTimeField
from wtforms.validators import DataRequired
from datetime import datetime

class ExpenseForm(FlaskForm):
    name = StringField('Expense Name', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('Food & Drinks', 'Food & Drinks'),
        ('Bills & Payments', 'Bills & Payments'),
        ('Entertainment', 'Entertainment'),
        ('Shopping', 'Shopping'),
        ('Transportation', 'Transportation'),
        ('Other', 'Other')
    ], validators=[DataRequired()])
    timestamp = DateTimeField('Date and Time', default=datetime.utcnow, format='%Y-%m-%d %H:%M:%S') 
    submit = SubmitField('Add Expense')
    