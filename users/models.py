from django.db import models
from django.contrib.auth.models import User
from PIL import Image

def get_default_category():
    return Category.objects.get_or_create(name='Не определена')

class Category(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)
    phone = models.CharField(max_length=13)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    description = models.CharField(max_length=10000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=11)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

