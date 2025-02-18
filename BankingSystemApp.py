# ****************************************************************************************
# Banking System Application with parent class BankAccount
# Banking System wihas two child classes CheckingAccount and SavingsAccount
# ****************************************************************************************
class BankAccount:

    # ************************************************************************************
    # Class constant for the default interest rate (2% expressed as decimal)
    # ************************************************************************************
    INTEREST_RATE = 0.02

    # ************************************************************************************
    # Static method to return the default interest rate
    # This method is invokable without instantiating the class.
    # ************************************************************************************
    @staticmethod
    def get_interest_rate():
        return BankAccount.INTEREST_RATE

    # ************************************************************************************
    # Constructor to initialize the account number, account holder, and balance
    # ************************************************************************************
    def __init__(self, account_number, account_holder, balance):
        # protected attributes using name mangling
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    # ************************************************************************************
    # Accessor methods for the encapsulated attributes
    # ************************************************************************************
    def get_account_number(self):
        return self.__account_number
    
    def get_account_holder(self):
        return self.__account_holder
    
    def get_balance(self):
        return self.__balance
    
    # ************************************************************************************
    # Method to calculate the balance after applying compound interest.
    # 'time' is the input number periods over which the interest is applied.
    # ************************************************************************************
    def calculate_balance(self, time):
        # Validate that time is a non-negative number
        if not isinstance(time, (int, float)) or time < 0:
            print("Invalid time period! Please enter a non-negative number.")
            return self.get_balance()
        self.__balance = self.__balance * ((1 + BankAccount.INTEREST_RATE) ** time)
        return self.__balance

    # ************************************************************************************
    # Method adds the specified amount to the account balance
    # ************************************************************************************
    def deposit(self, amount):
        # check if the amount is a valid number
        if not isinstance(amount, (int, float)):
            print("Invalid input! Please enter a valid number.")
            return False
        # check if the amount is positive
        if amount > 0:
            self.__balance += amount
            return True
        # print error message if the amount is not positive
        else:
            print("Invalid amount! Please enter a positive value.")
            return False

    # ************************************************************************************
    # Method for withdrawals that subtracts the specified amount from the account
    # balance if sufficient funds are available
    # ************************************************************************************
    def withdraw(self, amount):
        # check if the amount is a valid number
        if not isinstance(amount, (int, float)):
            print("Invalid input! Please enter a valid number.")
            return False
        # check if the amount is positive
        if amount <= 0:
            print("Invalid amount! Please enter a positive value.")
            return False
        # check if the amount exceeds the balance
        elif amount > self.__balance:
            print(f"Insufficient funds! You can withdraw up to ${self.__balance:.2f}.")
            return False
        # subtract the amount from the balance if sufficient funds are available
        else:
            self.__balance -= amount
            print(f"Withdrawal successful! New balance: ${self.__balance:.2f}")
            return True

    # ************************************************************************************
    # Method to return Bank Account details
    # ************************************************************************************
    def __str__(self):
        return (
            f"Account Type: Bank Account\n"
            f"Account Number: {self.__account_number}\n"
            f"Account Holder: {self.__account_holder}\n"
            f"Balance: ${self.__balance:.2f}"
        )

# ****************************************************************************************
# Child class CheckingAccount for the parent BankAccount class
# ****************************************************************************************
class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance):
        # Inherit all attributes from BankAccount
        super().__init__(account_number, account_holder, balance)
        # initialize overdraft limit
        self.overdraft_limit = 500

    # ************************************************************************************
    # Override the withdraw method to allow overdrafts up to the overdraft limit
    # ************************************************************************************
    def withdraw(self, amount):
        # check if the amount is a valid number
        if not isinstance(amount, (int, float)):
            print("Invalid input! Please enter a valid number.")
            return False
        # check if the amount is positive
        if amount <= 0:
            print("Invalid amount! Please enter a positive value.")
            return False
        # Get the current balance of the account
        current_balance = self.get_balance()
        # If the amount is within the available balance, proceed normally.
        if amount <= current_balance:
            self._BankAccount__balance -= amount
            print(f"Withdrawal successful! New balance: ${self.get_balance():.2f}")
            return True
        # Otherwise, allow an overdraft if within the limit.
        elif (amount - current_balance) <= self.overdraft_limit:
            self._BankAccount__balance = current_balance - amount
            print(f"Withdrawal successful with overdraft! New balance: ${self.get_balance():.2f}")
            return True
        # Print an error message if the withdrawal exceeds the overdraft limit.
        else:
            print(f"Error: Withdrawal exceeds overdraft limit. You can withdraw up to ${current_balance + self.overdraft_limit:.2f}.")
            return False

    # ************************************************************************************
    # Override the calculate_balance method for checking accounts.
    # Checking accounts do not earn interest, instead a monthly maintenance fee is subtracted.
    # ************************************************************************************
    def calculate_balance(self, time):
        # Validate that time is a non-negative number
        if not isinstance(time, (int, float)) or time < 0:
            print("Invalid time period! Please enter a non-negative number.")
            # return the balance without any changes
            return self.get_balance()
        # calculate monthly maintenance fee
        fee = 10 * time
        # subtract the fee from the balance
        self._BankAccount__balance = self.get_balance() - fee
        # return the updated balance
        return self.get_balance()

    # ************************************************************************************
    # Method to return Checking Account details (override parent class method)
    # ************************************************************************************
    def __str__(self):
        return (
            f"Account Type: Checking Account\n"
            f"Account Number: {self.get_account_number()}\n"
            f"Account Holder: {self.get_account_holder()}\n"
            f"Balance: ${self.get_balance():.2f}\n"
            f"Overdraft Limit: ${self.overdraft_limit:.2f}"
        )

# ****************************************************************************************
# child class SavingsAccount for the parent BankAccount class
# ****************************************************************************************
class SavingsAccount(BankAccount):
    # inherits all attributes and methods from the parent BankAccount class
    def __init__(self, account_number, account_holder, balance):
        # Inherit all attributes from BankAccount
        super().__init__(account_number, account_holder, balance)
        # initialize minimum balance
        self.minimum_balance = 100
        # initialize withdrawal count
        self.withdraw_count = 0
        
    # ************************************************************************************
    # Override the withdraw method to ensure withdrawals do not reduce the balance
    # below the minimum balance. Increments the withdrawal count on success.
    # ************************************************************************************
    def withdraw(self, amount):
        # check if the amount is a valid number
        if not isinstance(amount, (int, float)):
            print("Invalid input! Please enter a valid number.")
            return False
        # check if the amount is positive
        if amount <= 0:
            print("Invalid amount! Please enter a positive value.")
            return False
        # Get the current balance of the account
        current_balance = self.get_balance()
        # Check if the withdrawal would reduce the balance below the minimum
        if current_balance - amount < self.minimum_balance:
            print(f"Error: Withdrawal would reduce balance below the minimum of ${self.minimum_balance:.2f}.")
            return False
        # Allow the withdrawal if the balance remains above the minimum
        self._BankAccount__balance = current_balance - amount
        self.withdraw_count += 1
        print(f"Withdrawal successful! New balance: ${self.get_balance():.2f}")
        return True

    # ************************************************************************************
    # Override the calculate_balance method for savings accounts.
    # Applies interest using the parent's method and adds a $10 reward if no withdrawals
    # have occurred since the last calculation. Resets the withdrawal count afterward.
    # ************************************************************************************
    def calculate_balance(self, time):
        # Apply compound interest using the parent's calculation.
        new_balance = super().calculate_balance(time)
        # Add monthly reward if no withdrawals were made.
        if self.withdraw_count == 0:
            new_balance += 10
        self._BankAccount__balance = new_balance
        print(f"Balance after interest and reward: ${self.get_balance():.2f}")
        # Reset the withdrawal counter after calculating the balance.
        self.withdraw_count = 0
        return self.get_balance()

    # ************************************************************************************
    # Return a string representation of the SavingsAccount including minimum balance.
    # ************************************************************************************
    def __str__(self):
        return (
            f"SavingsAccount\n"
            f"Account Number: {self.get_account_number()}\n"
            f"Account Holder: {self.get_account_holder()}\n"
            f"Balance: ${self.get_balance():.2f}\n"
            f"Minimum Balance: ${self.minimum_balance:.2f}"
        )

# ****************************************************************************************
# test script to validate functionality
# ****************************************************************************************
interest_rate = BankAccount.get_interest_rate()
print(f"Default interest rate: {interest_rate:.2%}")

# checking = CheckingAccount(123, "Alice", 1000)
# print(checking)

account = BankAccount(123, "Alice", 1000)
print(account)
print("-----------------------------")

account_balance = account.get_balance()
print(f"Account balance: {account_balance}")

print("-----------------------------")
time_period = 12
print(f"The account balance is: {account.calculate_balance(time_period):.2f}")

print("-----------------------------")
# Create a BankAccount instance with an initial balance of $1000
account = BankAccount("123456", "John Doe", 1000.00)

# Test Case 1: Withdraw a valid amount (within balance)
print(f"Initial Balance: ${account.get_balance():.2f}")
account.withdraw(-200)  # Withdraw $200
account.withdraw(200)  # Withdraw $200
print(f"Balance after withdrawing $200: ${account.get_balance():.2f}")
account.withdraw("two hundred")  # Withdraw $200

# Test Case 2: Withdraw an amount larger than the balance
account.withdraw(900)  # Try to withdraw $900, should print "Insufficient funds!"
print(f"Balance after attempting to withdraw $900: ${account.get_balance():.2f}")

# Test Case 3: Withdraw exactly the remaining balance
account.withdraw(800)  # Withdraw exactly what's left
print(f"Balance after withdrawing all funds: ${account.get_balance():.2f}")

# Test Case 4: Withdraw from an empty account
account.withdraw(50)  # Try to withdraw from zero balance


