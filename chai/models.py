from django.db import models
from django.utils import timezone #to add time zone 
from django.contrib.auth.models import User #to link reviews to users

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

    rating = models.PositiveIntegerField(null=True)  #average rating based on user reviews
    description=models.TextField(default='')

    def __str__(self):
        return self.name  #When you print an instance of this model, 
    #it will return the name of the tea variety.otherwise it will show chaiVarity object (1) etc.


#review model to store user reviews for each chai variety
#many-to-one relationship between chaiVarity and chiaReview
class chaiReview(models.Model):
    chai_variety = models.ForeignKey(chaiVarity, on_delete=models.CASCADE, related_name='reviews')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  #assuming rating is from 1 to 5
    comment = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review for {self.chai_variety.name} by {self.user.username}'


   #store model to represent physical or online stores selling chai varieties
   # many-to-many relationship between chaiVarity and store 
    
class store(models.Model):   
     name = models.CharField(max_length=100)
     location = models.CharField(max_length=255)

     chai_varieties = models.ManyToManyField(chaiVarity, related_name='stores')  

     opening_hours = models.CharField(max_length=100)
     contact_info = models.CharField(max_length=100)

     def __str__(self):
            return self.name
        

       #model to represent certifications for chai varieties
       # one-to-one relationship between chaiVarity and chaiCertification 

class chaiCertification(models.Model):
    chai_certification=models.OneToOneField(chaiVarity, on_delete=models.CASCADE,
                                                 related_name='certification')
    
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateField()
    certification_body = models.CharField(max_length=100,null=True)


    def __str__(self):
            return f'{self.certification_body}certification for {self.chai_certification.name}'   

    


