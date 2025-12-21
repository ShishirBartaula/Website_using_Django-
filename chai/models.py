from django.db import models
from django.utils import timezone #to add time zone 


# Create your models here.

class chaiVarity(models.Model):
    CHAI_TYPE_CHOICES = [
        ('black', 'Black Tea'),
        ('green', 'Green Tea'),
        ('herbal', 'Herbal Tea'),
        ('oolong', 'Oolong Tea'),
        ('white', 'White Tea'),]
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='chai_images/')  #install Pillow for image field
    #want to install image so go to settings.py and add media settings
    
    price = models.DecimalField(max_digits=8, decimal_places=2,null=True) #null=True to make it optional
    #DecimalField is used for fixed-point decimal numbers, ideal for currency values.
    #best idea is make new class for price if you want to add more features like discount, tax etc.

    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=20, choices=CHAI_TYPE_CHOICES)
    description=models.TextField(default='')



    def __str__(self):
        return self.name  #When you print an instance of this model, 
    #it will return the name of the tea variety.otherwise it will show chaiVarity object (1) etc.
