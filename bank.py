class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance
    def deposit(self, money):
        if money < 0:
            self.balance += money
        print(f"you have successfully replenished your account,the amount is on the balance - {self.balance}")

    def withdraw(self, money):
        if money > self. balance:
            print(f"insufficient funds in the account")
        elif money <= self.balance:
            self.balance -= money
            print(f"you have successfully withdraw the money {money},account balance:{self.balance}")
    def all_balance(self):
        print(f"current balance - {self.balance}")
man = Account("89218921", 850)
man.all_balance()
man.withdraw(230)
man.withdraw(150)
man.withdraw(70)
man.deposit(6000)









