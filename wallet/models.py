from django.db import models
from accounts.models import CustomUser

class Wallet(models.Model):
    user=models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    current_balance= models.FloatField(default=0)
    loan_balance=models.FloatField(default=0)

    def deposit(self, value):
       
        self.transaction_set.create(
            value=value,
            running_balance=self.current_balance + value
        )
        self.current_balance += value
        self.save()

    def withdraw(self, value):
        print(value)
        print(self.current_balance)
        if value > self.current_balance:
            raise Exception('This wallet has insufficient balance.')

        self.transaction_set.create(
            value=-value,
            running_balance=self.current_balance - value
        )
        self.current_balance -= value
        self.save()

    def transfer(self, wallet, value):
        self.withdraw(value)
        wallet.deposit(value)
    
class Transaction(models.Model):
    # The wallet that holds this transaction.
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    # The value of this transaction.
    value = models.FloatField(default=0)

    # The value of the wallet at the time of this
    # transaction. Useful for displaying transaction
    # history.
    running_balance =models.FloatField(default=0)

    # The date/time of the creation of this transaction.
    created_at = models.DateTimeField(auto_now_add=True)