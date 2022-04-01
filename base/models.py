from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name


# Blogs Model
class Blog(models.Model):
    title = models.CharField(max_length=250)
    postDetails = models.TextField(max_length=2500)

    def __str__(self):
        return self.title
