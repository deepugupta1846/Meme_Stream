from django.db import models

# Create your models here.


class UserRecord(models.Model):
    profile_pic = models.ImageField(upload_to='photo/', default='static/app/images/ZZ5H.gif')
    Name = models.CharField(max_length=100, null=True)
    Gender = models.CharField(max_length=10, null=True)
    Email = models.EmailField(max_length=200, null=True, unique=True)
    Password = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.id}-{self.Name}"
class Post(models.Model):
    User_Name = models.ForeignKey(UserRecord, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Post_Image/')
    Caption = models.TextField()