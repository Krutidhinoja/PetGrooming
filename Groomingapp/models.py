from django.db import models

# Create your models here.

class Petdb(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    zipcode=models.IntegerField()

def __str__(self):
    return self.firstname

class Detaildb(models.Model):
    questions=models.CharField(max_length=100)
    visits=models.CharField(max_length=100)
    fileupload=models.FileField(upload_to="UploadedFiles")
    description=models.TextField()

def __str__(self):
    return self.questions