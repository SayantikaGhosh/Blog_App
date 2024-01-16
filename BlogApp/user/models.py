from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='Profile_pic')

    def __str__(self):
        return f"{self.user.username} profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

    # decrease the image size but  makes having issue as the image gets rotated
    # if img.height > 300 or img.width > 300:
    #     output_size = (200,200)
    #     img.thumbnail(output_size)
    #     img.save(self.image.path)
