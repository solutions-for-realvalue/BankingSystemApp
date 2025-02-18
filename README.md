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

