

---

# iSpendIT: Personal Finance Tracker

iSpendIT is a personal finance tracking application designed to help users manage their finances effectively. The app features account tracking, budget management, transaction categorization, and visualized data for financial insights.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Technologies Used](#technologies-used)  
4. [Setup and Installation](#setup-and-installation)  
5. [Usage](#usage)  
6. [Screenshots and Sections](#screenshots-and-sections)  
   - [Home Page Overview](#home-page-overview)  
   - [Login and Signup](#login-and-signup)  
   - [Other Pages](#other-pages)  
7. [API Documentation](#api-documentation)  
8. [Contributing](#contributing)  
9. [License](#license)  
10. [Contact](#contact)  

---

## Project Overview

iSpendIT simplifies financial management by allowing users to:
- Add and manage accounts.
- Set budgets and track expenses.
- Categorize transactions and view trends.
- Gain insights into spending and saving patterns through visualized data.

This project is live at:  
👉 **[iSpendIT on PythonAnywhere](https://ispendit.pythonanywhere.com/)**

The project comprises:
- A **Django-based web application** for managing finances.
- A **Flutter mobile app** for QR code-based attendance and finance tracking (future feature integration).

---

## Features

- **Account Overview**: Monitor balances for various accounts.
- **Budget Tracking**: Set a budget, track expenses, and get alerts for overruns.
- **Transaction Management**: Filter transactions by date, category, or type.
- **Categories and Subcategories**: Organize income and expenses into groups.
- **Data Visualization**: Gain insights through graphs and charts.
- **User Authentication**: Secure signup, login, and logout functionality.
- **Responsive Design**: Accessible across devices.

---

## Technologies Used

### Backend:
- **Django** (Python) for server-side logic and API handling.
- **SQLite** as the database (can be switched to PostgreSQL or MySQL).

### Frontend:
- **HTML5**, **CSS3**, **JavaScript** for the user interface.
- **Bootstrap** for responsive design.

### Mobile:
- **Flutter** for QR code-based attendance management.

### Additional Tools:
- **Django REST Framework** for API creation.
- **Chart.js** for data visualization.

---

## Setup and Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hirwacedric123/ispending.git
   cd ispending
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/macOS
   venv\Scripts\activate      # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

---

## Usage

- **Web App**: Access the dashboard at `http://127.0.0.1:8000/` or the hosted link: [https://ispendit.pythonanywhere.com/](https://ispendit.pythonanywhere.com/).  
- **Mobile App**: Use the Flutter app to manage finances on the go (planned feature).  

---

## Screenshots and Sections

### Home Page Overview

The **Home Page** provides a comprehensive view of the user's financial data, divided into the following sections:  
*(Detailed explanation provided earlier.)*  

---

### Login and Signup

#### 1. **Signup Page**
- **Purpose**: Allows new users to create an account.
- **Fields**:
  - Username
  - Email Address
  - Password (with confirmation)
- **Action**: Registers the user and redirects to the login page.

**Screenshot**: *(Add signup page screenshot here)*  

#### 2. **Login Page**
- **Purpose**: Enables registered users to log in to their dashboard.
- **Fields**:
  - Username or Email Address
  - Password
- **Action**: Authenticates the user and redirects to the home page upon success.

**Screenshot**: *(Add login page screenshot here)*  

#### 3. **Logout**
- **Purpose**: Securely logs the user out and redirects them to the login page.

---

### Other Pages

#### Add Account, Transaction Summary, and Budget Management  
*(Details provided earlier)*  

---

## API Documentation

### Endpoints
1. **`/api/accounts/`**: Retrieve or create accounts.  
2. **`/api/transactions/`**: Retrieve, create, or update transactions.  
3. **`/api/categories/`**: Manage categories and subcategories.  

*(Add detailed API documentation or a link to it.)*  

---

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:  
   ```bash
   git push origin feature/your-feature-name
   ```
5. Submit a pull request.  

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.  

---

## Contact

For questions, suggestions, or feedback, please contact:

- **Name**: Cedric Hirwa  
- **Email**: [your-email@example.com]  
- **GitHub**: [https://github.com/hirwacedric123](https://github.com/hirwacedric123)  

---
