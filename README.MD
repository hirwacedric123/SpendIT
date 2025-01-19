

---

# iSpendIT

iSpendIT is a robust web application for managing personal and organizational finances. It allows users to track income and expenses, categorize transactions, set budgets, and generate insightful reports to manage finances effectively. The application is built using Django for the backend and HTML, CSS, and JavaScript for the frontend. The project is hosted on PythonAnywhere, and the live application can be accessed [here](https://ispendit.pythonanywhere.com/).

---

## Features

### 1. **User Management**
   - **Account Creation**: Users can register for an account using a secure registration form.
   - **Login/Logout**: Access is restricted to authenticated users. Sessions are maintained securely, and users can log out at any time.
   - **User Roles**: Admins have additional privileges to manage other users, including editing user details.

### 2. **Account Management**
   - Users can add multiple accounts to manage their finances (e.g., Cash, Bank Account, Credit Card).
   - Each account is associated with a type (e.g., Savings, Checking, Credit) and displays the current balance.
   - Balances update dynamically based on transactions linked to each account.

### 3. **Category and Subcategory Management**
   - Organize income and expenses by creating categories and subcategories.
   - For example:
     - **Income Categories**: Salary, Freelancing, Investments
     - **Expense Categories**: Groceries, Utilities, Entertainment
   - Users can add, edit, or delete categories and subcategories as needed.

### 4. **Transactions**
   - Users can record transactions (income or expense) linked to specific accounts and categories.
   - Transaction details include:
     - Amount
     - Date
     - Category/Subcategory
     - Description (optional)
   - All transactions are displayed in a table with filters for easier searching and organization.

### 5. **Advanced Filters**
   - Dynamically filter transactions by:
     - Date range (e.g., filter by a specific week or month).
     - Category/Subcategory (e.g., see only transactions related to “Groceries”).
     - Transaction Type (Income or Expense).
   - These filters are powered by AJAX for a smooth user experience with no page reloads.

### 6. **Budget Management**
   - Set a budget to track your expenses against a predefined limit.
   - Displays:
     - Total Budget
     - Total Expenses
     - Remaining Budget
   - Alerts are shown if the user exceeds their budget.
   - Budget updates dynamically based on transactions.

### 7. **Reports and Visualizations**
   - Generate visualized reports (e.g., bar charts, pie charts) to analyze spending and income patterns.
   - Summaries include total expenses by category, income vs. expenses, and account balances over time.

### 8. **Real-Time Feedback**
   - If the remaining budget goes negative, users receive alerts to manage their spending.
   - Transaction forms dynamically update without refreshing the page, ensuring a smooth user experience.

---

## Live Demo

Access the live version of iSpendIT:  
🔗 [iSpendIT Live Application](https://ispendit.pythonanywhere.com/)

---

## Screenshots

_Add screenshots of the application here to showcase the design and functionality._

---

## Installation Guide

### Prerequisites
- Python 3.9 or later
- Django 4.2 or later
- SQLite (default Django database) or any supported database
- Node.js and npm (optional, for advanced frontend features)

### Steps to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/hirwacedric123/iSpendIT.git
   cd iSpendIT
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

---

## Technologies Used

### Backend:
- **Django**: Web framework
- **SQLite**: Database (default, can be switched to others like PostgreSQL)

### Frontend:
- **HTML/CSS/JavaScript**: Core frontend technologies
- **AJAX**: For dynamic, asynchronous interactions

### Hosting:
- **PythonAnywhere**: Hosting platform for Django applications

---

## Contributions

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push your changes:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

- **Creator**: [Hirwa Cedric](https://github.com/hirwacedric123)  
- **Live Application**: [iSpendIT](https://ispendit.pythonanywhere.com/)

For any questions, suggestions, or feedback, feel free to reach out!

---

## Acknowledgments

- Django for the robust framework
- PythonAnywhere for the hosting services
- OpenAI for development support

---

## Future Enhancements

- Integration with a mobile app (using Flutter).
- Enhanced data visualizations with chart libraries.
- Multi-currency and multi-language support.

---

