from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(default='My Bio',max_length=100)
    image = models.ImageField(default='default.jpeg',upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            img.thumbnail((500,500))
            img.save(self.image.path)
