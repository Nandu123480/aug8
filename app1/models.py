from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    rating=models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=50)
    price=models.IntegerField()
    genre=models.CharField(max_length=30)
    pic=models.ImageField(upload_to='media',null=True)
    date=models.DateTimeField(auto_now_add=True)
    cap=models.CharField(max_length=200,default='')


    author=models.ForeignKey('Author',on_delete=models.CASCADE)

    def __str__(self):
        return self.title+" "+self.author.name
