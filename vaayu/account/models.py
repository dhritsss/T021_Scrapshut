from django.db import models
# Create your models here.


class user(models.Model):
    user_id  = models.AutoField
    fname = models.CharField(max_length=30,null = False)
    lname = models.CharField(max_length=30,null=False)
    email = models.EmailField(null = False ,blank=False, unique=True)
    phone = models.IntegerField(null = False , blank=False, unique= True)
    password = models.CharField(null = False,max_length=25)
    Address = models.TextField(max_length=300)
    country = models.CharField(null = False,max_length=50)
    pincode = models.IntegerField(null = False)

class ngo(models.Model):
    ngo_id = models.AutoField
    ngo_name = models.CharField(max_length=50,null=False)
    ngo_email = models.EmailField(null = False,blank=False,unique=True)
    ngo_phone = models.IntegerField(null = False, blank=False,unique= True)
    ngo_pass = models.CharField(null = False,max_length=25)
    ngo_address = models.TextField(max_length=300)
    ngo_country = models.CharField(null = False,max_length=50)
    ngo_pincode = models.IntegerField(null =False)
    weblink = models.URLField()

class Equipments(models.Model):
    eqi_id = models.AutoField
    eqi_name = models.CharField(max_length=200)
    Price = models.FloatField()
    def __str__(self):
        return self.eqi_name

class Requirements(models.Model):
    ngo_id = models.ForeignKey(ngo,on_delete=models.CASCADE)
    eqi_id = models.ForeignKey(Equipments,on_delete=models.CASCADE)
    Quantity = models.IntegerField()


class Donations(models.Model):
    user_id = models.ForeignKey(user,on_delete=models.CASCADE)
    ngo_id = models.ForeignKey(ngo, on_delete=models.CASCADE)
    eqi_id = models.ForeignKey(Equipments, on_delete=models.CASCADE)
    Quantity = models.IntegerField()