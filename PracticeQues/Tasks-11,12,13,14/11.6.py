def create_wallet(name, balance):
    def deposit(amount):
        nonlocal balance
        if amount > 0:
            balance += amount
            print("Deposited", amount, ". Balance:", balance)
        else:
            print("Deposit must be positive")
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            print("Insufficient funds. Balance:", balance)
        else:
            balance -= amount
            print("Withdrew", amount, ". Balance:", balance)
    def statement():
        print(name + "'s balance:", balance)
    return deposit, withdraw, statement
deposit, withdraw, statement = create_wallet("Ravi", 1000)
statement()
deposit(500)
withdraw(2000)
withdraw(300)
deposit(-100)
statement()