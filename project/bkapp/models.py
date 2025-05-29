from django.db import models

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

        
class student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.name