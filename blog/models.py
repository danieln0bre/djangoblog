from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=25, blank=False, null=False)
    last_name = models.CharField(max_length=25, blank=False, null=False)
    email = models.EmailField(blank=True)


class Post(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    excerpt = models.CharField(max_length=200, blank=False, null=False)
    image_name = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])

class Tag(models.Model):
