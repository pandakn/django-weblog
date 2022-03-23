from unicodedata import name
from urllib import request
from django.urls import reverse
from django.db import models
from django.utils.text import slugify

class Contact(models.Model): 
    subject = models.CharField(max_length=100)
    email = models.EmailField() 
    sender = models.CharField(max_length=80)
    detail = models.TextField()

    def __str__(self):
        return self.subject


class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    

class Post(models.Model): #inherit มาจาก models.Model
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=80)
    short_description = models.CharField(max_length=160, null=True, blank=True)
    body = models.TextField()
    feature_pic = models.ImageField(upload_to="cover/", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('single-post', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


