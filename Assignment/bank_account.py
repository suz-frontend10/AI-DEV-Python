class BankAccount:
    """Bank Account"""

    # Static Attributes
    bank_name = "State Bank of India"
    total_accounts = 0
    interest_rate = 4.0
    MIN_BALANCE = 500
    _next_account_number = 1001


    def __init__(self, holder_name, account_type, initial_deposit, pin):
        """Constructor to initialize account details"""

        if initial_deposit < BankAccount.MIN_BALANCE:
            raise ValueError("Opening deposit below minimum balance")

        self.holder_name = holder_name            # Public
        self._account_number = BankAccount._next_account_number  # Protected
        self._account_type = account_type         # Protected
        self.__balance = initial_deposit          # Private
        self.__pin = pin                          # Private

        BankAccount._next_account_number += 1
        BankAccount.total_accounts += 1

    @property
    def account_number(self):
        """Returns account number (Read-only)"""
        return self._account_number

    @property
    def balance(self):
        """Returns account balance (Read-only)"""
        return self.__balance

    def deposit(self, amount):
        """Deposits money"""

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.__balance += amount
        return self.__balance

    def __verify_pin(self, pin):
        """Verifies PIN"""

        return self.__pin == pin

    def withdraw(self, amount, pin):#withdraw
        """Withdraws money"""

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if not self.__verify_pin(pin):
            raise ValueError("Incorrect PIN")

        if self.__balance - amount < BankAccount.MIN_BALANCE:
            raise ValueError(
                f"Insufficient funds. Minimum balance {BankAccount.MIN_BALANCE} must remain"
            )

        self.__balance -= amount
        return self.__balance

    def change_pin(self, old_pin, new_pin):#change pin
        """Changes PIN"""

        if not self.__verify_pin(old_pin):
            raise ValueError("Incorrect old PIN")

        if not (isinstance(new_pin, str) and len(new_pin) == 4 and new_pin.isdigit()):
            raise ValueError("New PIN must be exactly 4 digits")

        self.__pin = new_pin
        return "PIN changed successfully"

    def add_annual_interest(self):#nterest
        """Annual interest++"""

        interest = self.__balance * BankAccount.interest_rate / 100
        self.__balance += interest
        return interest

    @classmethod
    def get_total_accounts(cls):
        """Returns total number of accounts"""

        return cls.total_accounts

    @staticmethod
    def is_valid_amount(amount):
        """Checks whether amount is valid"""

        return isinstance(amount, (int, float)) and amount > 0


    def __str__(self):#string
        """Returns account details"""

        return (f"Account[{self._account_number}] "
                f"{self.holder_name} | "
                f"{self._account_type} | "
                f"Rs.{self.__balance:,.2f}")

    
def main():
    print(f"{'Bank':<25}: {BankAccount.bank_name}")

    a1 = BankAccount("Pragnya Sree", "Savings", 5000, "1234")
    a2 = BankAccount("Prakash", "Current", 20000, "5678")

    print(a1)
    print(a2)

    print(f"{'Total accounts':<25}: {BankAccount.get_total_accounts()}")

    print(f"{'Deposit 2000':<25}: {a1.deposit(2000)}")

    print(f"{'Withdraw 1500':<25}: {a1.withdraw(1500, '1234')}")

    interest = a1.add_annual_interest()
    print(f"{'Interest added':<25}: {interest}")
    print(f"{'Balance now':<25}: {a1.balance}")

    print(f"{'Change PIN':<25}: {a1.change_pin('1234', '4321')}")

    try:
        a1.withdraw(1000, "1111")
    except Exception as e:
        print(f"{'Blocked (wrong PIN)':<25}: {e}")

    try:
        a1.withdraw(6000, "4321")
    except Exception as e:
        print(f"{'Blocked (below min)':<25}: {e}")

    try:
        a1.deposit(-100)
    except Exception as e:
        print(f"{'Blocked (negative)':<25}: {e}")

    try:
        a1.balance = 999999
    except Exception as e:
        print(f"{'Blocked (write balance)':<25}: {e}")

if __name__=="__main__":
    main()