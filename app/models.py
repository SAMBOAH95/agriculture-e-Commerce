from django.db import models
from django.contrib.auth.models import User

# Create your models here.

REGION_CHOICES = (
    ("GOASO","AHAFO"),
    ("KUMASI","ASHANTI"),
    ("TECHIMAN","BONO EAST"),
    ("SUNYANI","BRONG AHAFO"),
    ("CAPE COAST","CENTRAL"),
    ("KOFORIDUA","EASTERN"),
    ("ACCRA","GREATER ACCRA"),
    ("NALERIGU","NORTH EAST"),
    ("TAMALE","NORTHERN"),
    ("DAMBAI","OTI"),
    ("DAMANGO","SAVANNAH"),
    ("BOLGATANGA","UPPER EAST"),
    ("WA","UPPER WEST"),
    ("TAKORADI","WESTERN"),
    ("SEFWI WIASO","WESTERN NORTH"),
    ("HO","VOLTA"),
)

CATEGORY_CHOICES=(
    ('AP','Apple'),
    ('MG','Mango'),
    ('WT','Watermelon'),
    ('BN','Banana'),
    ('GB','Green Beans'),
    ('CB','Cucumber'),
    ('ON','Onion'),
    ('SP','Sweet Potatoes'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    region = models.CharField(choices=REGION_CHOICES,max_length=100)
    def __str__(self):
        return self.name