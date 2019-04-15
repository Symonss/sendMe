from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.utils.html import escape, mark_safe

#oberriding the user class
class User(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    email= models.CharField(max_length=30,null=True,blank=True)
    first_name= models.CharField(max_length=30,null=True,blank=True)
    phone = models.PositiveIntegerField(default='0792799958')
    location = models.CharField(max_length=25, default='Kisumu')
    gender = models.CharField(max_length=150, default= 'Female')

    def __str__(self):
        return self.first_name

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    number = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.number

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Employer.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.employer.save()



class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image=models.CharField(max_length=30)
    id=models.CharField(max_length=30)
    good_certificate=models.CharField(max_length=30)
    proof =models.CharField(max_length=30)
    supporting_document = models.CharField(max_length=30)
    descriptio= models.TextField()


    def __str__(self):
        return self.descrition



class Jobs(models.Model):
    title = models.CharField(max_length=50, default='TV Mounting')
    job_description =models.TextField(default=
    'This job should be done as first as posible, can\'t wait for the bids',max_length=300)
    lower_range = models.IntegerField(default=500)
    upper_range = models.IntegerField(default=15000)
    Employer= models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='my_salons')
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_salons' ,blank=True, null=True)
    location =models.CharField(max_length=50, default='Kisumu')
    published_date= models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image=models.CharField(max_length=30)
    id=models.CharField(max_length=30)
    good_certificate=models.CharField(max_length=30)
    proof =models.CharField(max_length=30)
    supporting_document = models.CharField(max_length=30)
    descriptio= models.TextField()


    def __str__(self):
        return self.descrition
