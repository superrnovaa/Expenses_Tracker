# Expense Tracker

## Overview

The Expense Tracker is a web application that allows users to track their expenses over time. Users can add, view, and categorize their expenses, as well as visualize their spending patterns through charts. The application provides a user-friendly interface and utilizes modern web technologies.

## Technologies Used

- **Frontend**: 
  - React.js: A JavaScript library for building user interfaces.
  - Chart.js: A library for creating interactive charts.
  - Axios: A promise-based HTTP client for making API requests.
  - CSS: For styling the application.

- **Backend**: 
  - Flask: A lightweight WSGI web application framework for Python.
  - SQLite: A lightweight database for storing expense data.

## Features

- Add new expenses with details such as name, amount, and category.
- View a list of expenses for the selected month and year.
- Visualize accumulated expenses over the month using a line chart.
- Display summary cards for total expenses by category and overall total.

## Installation

### Prerequisites

- Node.js (v14 or higher)
- Python (v3.6 or higher)
- Flask
- SQLite


### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd expense-tracker-frontend
   ```

2. Install the required packages:

   ```bash
   npm install
   ```

3. Start the React application:

   ```bash
   npm start
   ```

### Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd expense-tracker-backend
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

### API Endpoints

- `GET /api/expenses`: Retrieve all expenses.
- `POST /api/expenses`: Add a new expense.

## Usage

1. Open your web browser and navigate to `http://localhost:3000` to access the Expense Tracker application.
2. Use the form to add new expenses.
3. Select the month and year to view your transaction history.
4. Hover over the chart to see detailed information about your expenses.



