from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # profile_pic = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username

class Test(models.Model):
    category = models.CharField(max_length = 264,default = 'category')
    teacher_name = models.CharField(max_length = 264,default = 'teacher_name')
    questiona = models.CharField(max_length = 264,default = 'question')
    optiona1 = models.CharField(max_length = 264,default = 'opt1')
    optiona2 = models.CharField(max_length = 264,default = 'opt2')
    optiona3 = models.CharField(max_length = 264,default = 'opt3')
    optiona4 = models.CharField(max_length = 264,default = 'opt4')
    option_a_correct = models.CharField(max_length = 264,default = 'opt_correct')
    questionb = models.CharField(max_length = 264,default = 'question')
    optionb1 = models.CharField(max_length = 264,default = 'opt1')
    optionb2 = models.CharField(max_length = 264,default = 'opt2')
    optionb3 = models.CharField(max_length = 264,default = 'opt3')
    optionb4 = models.CharField(max_length = 264,default = 'opt4')
    option_b_correct = models.CharField(max_length = 264,default = 'opt_correct')
    questionc = models.CharField(max_length = 264,default = 'question')
    optionc1 = models.CharField(max_length = 264,default = 'opt1')
    optionc2 = models.CharField(max_length = 264,default = 'opt2')
    optionc3 = models.CharField(max_length = 264,default = 'opt3')
    optionc4 = models.CharField(max_length = 264,default = 'opt4')
    option_c_correct = models.CharField(max_length = 264,default = 'opt_correct')
    questiond = models.CharField(max_length = 264,default = 'question')
    optiond1 = models.CharField(max_length = 264,default = 'opt1')
    optiond2 = models.CharField(max_length = 264,default = 'opt2')
    optiond3 = models.CharField(max_length = 264,default = 'opt3')
    optiond4 = models.CharField(max_length = 264,default = 'opt4')
    option_d_correct = models.CharField(max_length = 264,default = 'opt_correct')
    questione = models.CharField(max_length = 264,default = 'question')
    optione1 = models.CharField(max_length = 264,default = 'opt1')
    optione2 = models.CharField(max_length = 264,default = 'opt2')
    optione3 = models.CharField(max_length = 264,default = 'opt3')
    optione4 = models.CharField(max_length = 264,default = 'opt4')
    option_e_correct = models.CharField(max_length = 264,default = 'opt_correct')
    appeared_by = models.TextField(blank = True)
    scores = models.TextField(blank = True)
    def __str__(self):
        return self.category

class Scores(models.Model):
    test_pk = models.CharField(max_length = 264,default = 'test')
    username = models.CharField(max_length = 264,default = 'username')
    score = models.CharField(max_length = 264,default = 'score')

# class Users(models.Model):
#
#     name = models.CharField(max_length = 264, unique = True,
#
#     )
#     email  = models.EmailField()
#     password = models.CharField(max_length = 264)
