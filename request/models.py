from django.db import models

# Create your models here.


class LoanRequest(models.Model):

    PENDING ='Pending'
    FUNDED  ='Funded'
    COMPLETED = 'Completed'
    RATE_FEES ='RATE'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (FUNDED , 'Funded'),
        (COMPLETED,'Completed'),
    ]

    WHAT_FOR_CHOICES = [
        (RATE_FEES,'RATE') ,   
    ]
    
    user=models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    loan_ammount = models.FloatField()
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    what_for = models.CharField(choices=WHAT_FOR_CHOICES, max_length=50)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50,default=PENDING)
    loan_period=models.IntegerField()
    created_at = models.DateField( auto_now=True, auto_now_add=False)

   


class LoanOffer(models.Model):
    DEFAULT='Notselected'
    APPROVED ='Approved'
    REFUSED  ='Refused'
    STATUS_CHOICES = [
        (DEFAULT,'Default'),
        (APPROVED, 'Approved'),
        (REFUSED , 'Refused'),
    ]
    user=models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    request=models.ForeignKey(LoanRequest, on_delete=models.CASCADE)
    annual_interest_rate = models.IntegerField()
    status=models.CharField(choices=STATUS_CHOICES, max_length=50,default=DEFAULT)