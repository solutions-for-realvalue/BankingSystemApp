# 🏦 Banking System Application  

## 📖 Table of Contents

- [Overview](#-overview)  
- [Features](#-features)  
- [Technologies Used](#-technologies-used)  
- [Getting Started](#-getting-started)  
- [Usage](#-usage)  
- [Class Structure](#-class-structure)  
  - [BankAccount (Parent Class)](#bankaccount-parent-class)  
  - [CheckingAccount (Child Class)](#checkingaccount-child-class)  
  - [SavingsAccount (Child Class)](#savingsaccount-child-class)  
- [Testing](#-testing)  
- [Contributing](#-contributing)  
- [License](#-license)  
- [Contact](#-contact)  

---

## 🌟 Overview  

This **Banking System Application** is a Python-based simulation of a banking environment with different types of accounts. It leverages **Object-Oriented Programming (OOP)** principles such as **inheritance, encapsulation, method overriding, and data validation** to model realistic banking operations.

The system consists of a **parent class `BankAccount`** and two **child classes `CheckingAccount` and `SavingsAccount`** that introduce additional features such as overdraft limits, minimum balance requirements, and special interest calculations.

---

## 🚀 Features  

✅ **BankAccount Class:**  
- Interest rate management  
- Deposits and withdrawals with validation  
- Balance calculations  

✅ **CheckingAccount Class:**  
- Overdraft protection up to $500  
- Monthly maintenance fee deduction  
- No interest calculations  

✅ **SavingsAccount Class:**  
- Minimum balance requirement ($100)  
- Monthly reward for no withdrawals  
- Interest applied to balance  

✅ **Robust Data Validation:**  
- Prevents negative deposits  
- Ensures withdrawals do not exceed limits  

✅ **Readable Output:**  
- `__str__()` method for detailed account representation  

---

## 🛠️ Technologies Used  

- **Python 3.x**  
- **OOP Concepts**: Inheritance, Method Overriding, Encapsulation  
- **Custom Validations & Error Handling**  

---

## 📦 Getting Started  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/solutions-for-realvalue/VoiceRecipeSearchSystem.git
cd BankingSystemApplication
```

### 2️⃣ Run the Script  

```bash
python banking_system.py
```

---

## 🎯 Usage  

### 💰 Creating Accounts  

```python
# Creating a Checking Account and a Savings Account
checking_acc = CheckingAccount("001", "Alice", 2000)
savings_acc = SavingsAccount("002", "Bob", 5000)
```

### 📥 Depositing Funds  

```python
checking_acc.deposit(500)  # Adds $500 to checking account
savings_acc.deposit(1000)  # Adds $1000 to savings account
```

### 📤 Withdrawing Funds  

```python
checking_acc.withdraw(2500)  # Allows overdraft up to $500
savings_acc.withdraw(200)  # Ensures balance does not fall below $100
```

### 🏦 Calculating Balance After Time Passes  

```python
checking_acc.calculate_balance(6)  # Applies maintenance fees over 6 months
savings_acc.calculate_balance(6)  # Applies interest and rewards (if eligible)
```

### 📜 Printing Account Details  

```python
print(checking_acc)
print(savings_acc)
```

---

## 📌 Class Structure  

### **BankAccount (Parent Class)**  
✅ **Attributes:**  
- `INTEREST_RATE` (2%) - Constant interest rate for all accounts  
- `account_number` - Unique identifier for the account  
- `account_holder` - Name of the account holder  
- `balance` - Current account balance  

✅ **Methods:**  
- `get_interest_rate()` - Returns the interest rate  
- `calculate_balance(time)` - Updates balance based on interest over time  
- `deposit(amount)` - Adds funds to the account  
- `withdraw(amount)` - Removes funds if sufficient balance is available  

---

### **CheckingAccount (Child Class)**  
✅ **Additional Attributes:**  
- `overdraft_limit` (Default: $500)  

✅ **Overridden Methods:**  
- `withdraw()` - Allows overdrafts up to a limit  
- `calculate_balance()` - Deducts a **$10 maintenance fee** per month  

---

### **SavingsAccount (Child Class)**  
✅ **Additional Attributes:**  
- `minimum_balance` (Default: $100)  
- `withdrawal_count` - Tracks number of withdrawals  

✅ **Overridden Methods:**  
- `withdraw()` - Prevents withdrawals below the minimum balance  
- `calculate_balance()` - Applies interest and a **$10 reward** if no withdrawals occurred  

---

## 🛠️ Testing  

A **test script** is included to verify that all features work correctly. The test script:  

✅ Prints the **current interest rate**  
✅ Creates **Checking & Savings Accounts**  
✅ Tests **deposits and withdrawals**  
✅ Ensures **withdrawal rules are enforced**  
✅ Applies **interest & fees correctly**  
✅ Displays **account details after each transaction**  

To run the tests:

```bash
python test_banking.py
```

---

