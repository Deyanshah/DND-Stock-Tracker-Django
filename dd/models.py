from django.db import models

# Create your models here.
class Customer(models.Model):
    """Model representing a customer."""
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    year_batch = models.CharField(max_length=10)
    password=models.CharField(max_length=120,default='')
    level=models.IntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the Customer model."""
        return f'{self.cname}'

class Inventory(models.Model):
    """Model representing an inventory item."""
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    cp = models.DecimalField(max_digits=10, decimal_places=2)
    sp = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the Inventory model."""
        return f'{self.pname}'

class Order(models.Model):
    """Model representing an order."""
    oid = models.AutoField(primary_key=True)
    pid = models.ForeignKey(Inventory, models.CASCADE)
    cid = models.ForeignKey(Customer, models.CASCADE)
    quantity = models.IntegerField()
    order_date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the Order model."""
        return f'Order {self.oid}'

class Transaction(models.Model):
    """Model representing a transaction."""
    cid = models.ForeignKey(Customer, models.CASCADE)
    oid = models.AutoField(primary_key=True)
    pid = models.ForeignKey(Inventory, models.CASCADE)
    paid_status = models.BooleanField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date_time = models.DateTimeField(auto_now=True)
    
