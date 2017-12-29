from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)   #first one is a link to User Model in django
    description = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username + '-' + self.user.get_full_name()

#we can use signals to perform certian actions(run certain chunk of codes if any defined changes to database is detected
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(receiver=create_profile, sender=User, )
