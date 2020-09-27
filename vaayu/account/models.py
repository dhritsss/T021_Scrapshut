from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Donar(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="",related_name="profile")
    phone = models.IntegerField(unique= True,blank=False,null=False)
    Address = models.TextField(max_length=300,null=False)
    country = models.CharField(max_length=50,null=False)
    pincode = models.IntegerField()
    print()
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Donar.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.donar.save()
class NGO(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    ngo_Address = models.TextField(max_length=300,null=False)
    country = models.CharField(max_length=50,null= False)
    pincode = models.IntegerField()
    weblink = models.URLField()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            NGO.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

"""
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(

            email=self.normalize_email(email),

        )

        if kwargs.get("is_NGO"):
            user.is_NGO = True
            user.address_line1 = kwargs['address_line1']
            user.country = kwargs['country']
            user.pincode = kwargs['pincode']
            user.ngo_name = kwargs['ngo_name']
            user.weblink = kwargs['weblink']
        elif kwargs['is_Donor']:
            user.is_NGO = False
            user.address_line1 = kwargs['address_line1']
            user.country = kwargs['country']
            user.pincode = kwargs['pincode']
            user.first_name = kwargs['first_name']
            user.last_name = kwargs['last_name']
            user.username = kwargs['username']

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            is_NGO=False,
            is_Donor=False

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
"""
"""
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
"""
class Equipments(models.Model):
    eqi_id = models.AutoField
    eqi_name = models.CharField(max_length=200)
    Price = models.FloatField()
    def __str__(self):
        return self.eqi_name

class Requirements(models.Model):
    ngo_id = models.ForeignKey(NGO,on_delete=models.CASCADE)
    eqi_id = models.ForeignKey(Equipments,on_delete=models.CASCADE)
    Quantity = models.IntegerField()


class Donations(models.Model):
    user_id = models.ForeignKey(Donar,on_delete=models.CASCADE)
    ngo_id = models.ForeignKey(NGO, on_delete=models.CASCADE)
    eqi_id = models.ForeignKey(Equipments, on_delete=models.CASCADE)
    Quantity = models.IntegerField()

