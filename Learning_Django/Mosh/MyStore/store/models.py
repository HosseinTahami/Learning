from django.db import models

"""primary_key:
    django create primary key by default for each class 
    but if you want to do it your self you can put the
    primary_key in the arguments of the Field!
"""
# Create your models here.
class Product(models.Model):
    # sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    # we want 6 digit and 2 decimals at maximum : 9999.99
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    """
    auto_now=True: each time we update an item of this class
                    django automatically stores current datetime
     
    auto_now_add=True: only the first time that an item from 
                        this class is created django will
                        store datetime automatically
    """
    last_update = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD ='G'
    MEMBERSHIP_CHOICES = [
        ('B', MEMBERSHIP_BRONZE),
        ('S', MEMBERSHIP_SILVER),
        ('G', MEMBERSHIP_GOLD),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # unique=True means it can't be duplicated
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    # null=True means it can be empty
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOICES,
        default=MEMBERSHIP_BRONZE,
        )

class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        ('P', PAYMENT_PENDING),
        ('C', PAYMENT_COMPLETE),
        ('F', PAYMENT_FAILED),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1,
        choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_PENDING,
        )
    