# Finsight - AI-Powered Personal Finance Tracker

Finsight is an AI-powered personal finance tracker built with Streamlit and Python. Features user authentication, expense/income logging, interactive charts, and FinBot - an AI assistant using Cohere for budgeting advice. Uses SQLite databases and Plotly visualizations for secure, multi-user financial management.

## 🚀 Features

- **User Authentication**: Secure login and registration system
- **Expense & Income Tracking**: Log transactions with categories and descriptions
- **Financial Reports**: Interactive charts and visualizations using Plotly
- **AI Assistant (FinBot)**: Get personalized budgeting advice powered by Cohere AI
- **Multi-user Support**: Each user has their own secure database
- **Real-time Balance**: Automatic calculation of account balance
- **Data Visualization**: Pie charts, bar charts, and trend analysis

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: SQLite
- **AI**: Cohere API
- **Visualization**: Plotly
- **Authentication**: Custom implementation with password hashing

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Finsight
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the root directory
   - Add your Cohere API key:
     ```
     COHERE_API_KEY=your_cohere_api_key_here
     ```

5. **Run the application**
   ```bash
   streamlit run Home.py
   ```

## 📖 Usage

1. **Registration**: Create a new account or login with existing credentials
2. **Transaction Logging**: Use the "Transaction Log" page to add expenses and income
3. **View Expenses**: Check your transaction history in the "View Expenses" page
4. **Financial Reports**: Analyze your finances with interactive charts in the "Report" page
5. **AI Assistant**: Chat with FinBot for personalized financial advice

## 📸 Screenshots

### Login Page
![Login Page](assets/screenshots/login.png)
*Secure user authentication interface*

### Dashboard
![Dashboard](assets/screenshots/dashboard.png)
*Main dashboard showing current balance and quick actions*

### Transaction Logging
![Transaction Log](assets/screenshots/transaction_log.png)
*Add expenses and income with detailed categorization*

### Financial Reports
![Financial Reports](assets/screenshots/reports.png)
*Interactive charts showing expense breakdown and trends*

### AI Assistant (FinBot)
![FinBot](assets/screenshots/finbot.png)
*AI-powered financial assistant for budgeting advice*

## 🔧 Project Structure

```
Finsight/
├── Home.py                 # Main application entry point
├── auth.py                 # Authentication module
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in git)
├── .gitignore             # Git ignore rules
├── pages/                 # Streamlit pages
│   ├── 1_➕_Transaction_Log.py
│   ├── 2_📖_View_Expenses.py
│   └── 3_📊_Report.py
├── utils/                 # Utility modules
│   ├── __init__.py
│   ├── expenseTracker.py  # Core expense tracking logic
│   └── finbot.py         # AI assistant module
├── assets/                # Static assets
│   └── screenshots/       # Screenshots for README
└── img/                   # Static images
```

## 🤖 FinBot - AI Assistant

FinBot is powered by Cohere's advanced language models and provides:
- Personalized budgeting advice
- Financial insights based on your transaction history
- Savings recommendations
- Expense analysis and suggestions

## 🔒 Security

- Passwords are hashed using SHA-256
- Each user has their own SQLite database
- API keys are stored securely in environment variables
- Sensitive files are excluded from version control

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Streamlit for the amazing web app framework
- Cohere for AI capabilities
- Plotly for data visualization
- SQLite for lightweight database management

---

**Note**: Make sure to add your Cohere API key to the `.env` file before running the application. The AI features will be disabled if the API key is not configured.
