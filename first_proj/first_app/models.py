from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length = 100,unique = True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length = 100,unique = True)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class Branch(models.Model):
    branch = models.CharField(max_length = 100,unique = True)

    def __str__(self):
        return self.branch

class StudentDetails(models.Model):
    branch = models.ForeignKey(Branch,on_delete = models.CASCADE)
    roll = models.CharField(max_length = 100, unique = True)
    name = models.CharField(max_length = 100, unique = True)
    def __str__(self):
        return self.roll

class StudentGrade(models.Model):
    roll = models.ForeignKey(StudentDetails,on_delete = models.CASCADE)
    grade = models.CharField(max_length = 100)
    result = models.CharField(max_length = 100)

    def __str__(self):
        return self.result

class LocUser(models.Model):
    firstName = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)

    def __str__(self):
        return self.firstName

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank = True)


    def __str__(self):
        return self.user.username
