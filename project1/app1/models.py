from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=50)
    user_number = models.IntegerField()
    user_date = models.DateField()
    profile_pic = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return self.username
