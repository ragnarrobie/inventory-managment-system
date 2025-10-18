from django.db import models
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