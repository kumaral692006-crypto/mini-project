class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")


class ATM(BankAccount):
    def show_details(self):
        print("\n----- Account Details -----")
        print(f"Name: {self.name}")
        print(f"Available Balance: {self.get_balance()}")


acc = ATM("kumara", 7000000)

acc.show_details()
acc.deposit(5000)
acc.withdraw(2000)
acc.show_details()