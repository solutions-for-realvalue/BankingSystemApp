# Banking System Application that consist of parent class
# Banking System with two child classes CheckingAccount and SavingsAccount
class BankAccount:
    # class constant for the default interest rate (2% expressed as decimal)
    INTEREST_RATE = 0.02

    # static method to return the default interest rate
    @staticmethod
    def get_interest_rate():
        return BankAccount.INTEREST_RATE

    # constructor to initialize the account number, account holder, and balance
    def __init__(self, account_number, account_holder, balance):
        # protected attributes using name mangling
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    # accessor methods for the encapsulated attributes
    def get_account_number(self):
        return self.__account_number
    
    def get_account_holder(self):
        return self.__account_holder
    
    def get_balance(self):
        return self.__balance
    
    # method calculates the balance (takes time as input parameter to calculate
    #  the balance after applying compound interest)
    def calculate_balance(self, time):
        self.__balance = self.__balance * ((1 + BankAccount.INTEREST_RATE) ** time)
        return self.__balance

    # method adds the specified amount to the account balance
    def deposit(self, amount):
        self.__balance += amount

    # method for withdrawals that subtracts the specified amount from the account
    # balance if sufficient funds are available
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")


# child class
class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = 500

# child class 
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = 0.04




interest_rate = BankAccount.get_interest_rate()
print(f"Default interest rate: {interest_rate:.2%}")

# checking = CheckingAccount(123, "Alice", 1000)
# print(checking)

account = BankAccount(123, "Alice", 1000)
account_balance = account.get_balance()
print(f"Account balance: {account_balance}")

time_period = 12
print(f"The account balance after {time_period} years is: {account.calculate_balance(time_period)}")






