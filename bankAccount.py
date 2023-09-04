class bank_account:
    def __init__(self,acc_no,balance):
        self._acc_no = acc_no
        self._balance = balance
    def withdraw(self,amount):
        if amount > self._balance:
            print("Your Balance is too low!")
        else:
            a = self._balance
            self._balance = self._balance - amount 
            print(f"Account Number: {self._acc_no}")
            print(f"Previous Balance: {a}")
            print(f"Withdraw: {amount}")
            print(f"Current Balance: {self._balance}")

rahul = bank_account(100,50000)
rahul.withdraw(60000)

sara = bank_account(200,100000)
sara.withdraw(50000)