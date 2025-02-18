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







