class BankAccount:
    # Class Attributes
    bank_name = "National Bank"
    total_accounts = 0
    total_bank_balance = 0

    def __init__(self, account_holder, initial_deposit=0):
        # Instance Attributes
        self.account_holder = account_holder
        self.balance = initial_deposit

        # Update Class Attributes
        BankAccount.total_accounts += 1
        BankAccount.total_bank_balance += initial_deposit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            BankAccount.total_bank_balance += amount
            print(f"Deposited ${amount} successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance. Withdrawal denied.")
        else:
            self.balance -= amount
            BankAccount.total_bank_balance -= amount
            print(f"Withdrew ${amount} successfully.")

    def display_account_info(self):
        print("----- Account Information -----")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")
        print("--------------------------------")

    @classmethod
    def display_bank_summary(cls):
        print("===== Bank Summary =====")
        print(f"Bank Name: {cls.bank_name}")
        print(f"Total Accounts: {cls.total_accounts}")
        print(f"Total Bank Balance: ${cls.total_bank_balance}")
        print("========================")