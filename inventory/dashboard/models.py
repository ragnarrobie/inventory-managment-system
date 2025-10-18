from django.db import models
from django.contrib.auth.models import User
CATEGORY = (
    ('Stationary','Stationary'),
    ('Electronics','Electronics'),
    ('Food','Food'),
)
class product(models.Model):
    name = models.CharField(max_length = 100, null = True)
    category = models.CharField(max_length = 20,null = True)
    Quantity = models.PositiveBigIntegerField(null = True)
    
    def __str__(self):
        return f'{self.name}-{self.Quantity}'
class Order(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, null = True)
    staff = models.ForeignKey(User, models.CASCADE, null =True)
    order_quantity= models.PositiveBigIntegerField(null = True)
    date = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'