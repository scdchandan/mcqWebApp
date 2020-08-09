from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username

class Question(models.Model):
    category = models.CharField(max_length = 264,default = 'category')
    question = models.CharField(max_length = 264,default = 'question')
    option1 = models.CharField(max_length = 264,default = 'opt1')
    option2 = models.CharField(max_length = 264,default = 'opt2')
    option3 = models.CharField(max_length = 264,default = 'opt3')
    option4 = models.CharField(max_length = 264,default = 'opt4')
    option_correct = models.CharField(max_length = 264,default = 'opt_correct')
    def __str__(self):
        return self.question

# class Users(models.Model):
#
#     name = models.CharField(max_length = 264, unique = True,
#
#     )
#     email  = models.EmailField()
#     password = models.CharField(max_length = 264)
