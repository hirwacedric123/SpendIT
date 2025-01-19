
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

The project comprises:
- A **Django-based web application** for managing finances.
- A **Flutter mobile app** for on-the-go access to QR codes and attendance (future feature integration).

---

## Features

- **Account Overview**: Monitor balances for various accounts.
- **Budget Tracking**: Set a budget, track expenses, and get alerts for overruns.
- **Transaction Management**: Filter transactions by date, category, or type.
- **Categories and Subcategories**: Organize income and expenses into groups.
- **Data Visualization**: Gain insights through graphs and charts.
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
   git clone https://github.com/your-repo-url/ispending.git
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

- **Web App**: Access the dashboard at `http://127.0.0.1:8000/`.
- **Mobile App**: Use the Flutter app to scan QR codes and manage finances on the go.

---

## Screenshots and Sections

### Home Page Overview

The **Home Page** provides a comprehensive view of the user's financial data, divided into the following sections:

1. **Header Section**  
   *(Explanation as provided earlier)*  

2. **Account Overview Section**  
   *(Explanation as provided earlier)*  

3. **Budget Overview Section**  
   *(Explanation as provided earlier)*  

4. **Recent Transactions Section**  
   *(Explanation as provided earlier)*  

5. **Categories and Subcategories Section**  
   *(Explanation as provided earlier)*  

### Other Pages

#### 1. **Add Account Page**
- **Purpose**: Allows users to add new financial accounts.
- **Fields**:
  - Account Name
  - Account Type (e.g., Savings, Checking)
  - Initial Balance
- **Action**: Adds a new account to the database.

**Screenshot**:  
*(Add screenshot of the Add Account page)*

#### 2. **Transaction Summary Page**
- **Purpose**: Visualizes transaction data through graphs and charts.
- **Components**:
  - Pie charts for category-wise expenses.
  - Line charts for monthly trends.

**Screenshot**:  
*(Add screenshot of the Transaction Summary page)*

#### 3. **Manage Budget Page**
- **Purpose**: Enables users to set or update their monthly budget.
- **Fields**:
  - Total Budget Amount
  - Budget Start and End Dates

**Screenshot**:  
*(Add screenshot of the Manage Budget page)*

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

- **Name**: [Your Name]  
- **Email**: [your-email@example.com]  
- **GitHub**: [https://github.com/your-username](https://github.com/your-username)

---

