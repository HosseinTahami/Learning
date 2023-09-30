from django.db import models

"""primary_key:
    django create primary key by default for each class 
    but if you want to do it your self you can put the
    primary_key in the arguments of the Field!
"""

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    
class Collection(models.Model):
    title = models.CharField(max_length=255)
    

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
    collection = models.ForeignKey(
        Collection,
        on_delete=models.PROTECT
        )
    """
    ManyToManyField: we use this in Many To Many Relations and we should
                     decide were to put it <inside which class> and the 
                     best answer is inside the one that is more important
                     for us !
    """
    promotions = models.ManyToManyField(Promotion)

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
    customer = models.ForeignKey(
    Customer,
    on_delete=models.CASCADE,
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.ProtectedError
    )
class Address(models.Model):
    """
    There is a one to one relationship between
    Customer and Address so each Customer should
    only have one and only Address and each Address
    should belongs to one and only one Customer!
    """
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # Customer is the parent of the Address Entity
    ''' on_delete is to set the behavior of Address Entity when
        the Customer entity is deleted and CASCADE means that 
        the address will be deleted too.
        
        primary_key is there so that django do not make
        an ID for the Address entity by default.
    '''
    
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        primary_key=True,
        )


class Item(models.Model):
    pass

class Cart(models.Model):
    # auto_now_add will save the time only for the first time
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT
        )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
        )
    quantity = models.PositiveSmallIntegerField()
    """
    The reason we have unit_price here too is because
    the price of an Item always change through time
    so we want know the price of the Item at the time
    of the order.
    """
    unit_price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
        )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
        )
    quantity = models.PositiveSmallIntegerField()