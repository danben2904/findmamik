from django.db import models
from django.contrib.auth.models import User

def image_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.user.id, filename)


class Seeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='None')
    second_name = models.CharField(max_length=100, default='None')
    email = models.CharField(max_length=100)
    is_mamik = models.BooleanField(default=False)
    is_free = models.BooleanField(default=True)
    age = models.IntegerField(default=-1)
    salary = models.IntegerField(default=0)
    country = models.CharField(max_length=4, default='None')
    loyalty_points = models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to=image_directory_path, default="olikpipi.png")

    def __str__(self):
        return self.user.username
