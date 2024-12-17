from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


class Ourteam(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField( blank=True, null=True)
    phone = models.CharField(max_length=20,  blank=True, null=True)
    message = models.TextField()
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')  # ForeignKey to User
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    short_description=CKEditor5Field('Text', config_name='short description')
    description=CKEditor5Field('Text', config_name='description')
    slug = models.SlugField(unique=True, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title or "Untitled Blog"


# Automatically generate the slug from the title
@receiver(pre_save, sender=Blog)
def auto_generate_slug(sender, instance, **kwargs):
    if instance.title and not instance.slug:
        instance.slug = slugify(instance.title)