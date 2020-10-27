from django.db import models

# Create your models here.

class Device(models.Model):

    ltype = models.CharField(max_length=100,blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE','Item is available for purchas'),
        ('SOLD','This item cannot be purchased'),
        ('RESTOCKING','Item is on restocking')
    )

    status = models.CharField(max_length=10,choices=choices,default='SOLD')
    issues = models.CharField(max_length=100,default='no issues')

    class Meta:
        abstract = True


    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.ltype,self.price)

class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass



