from django.db import models

# Create your models here.
class Student(models.Model):
    Courses=[
        ('AIML','AIML'),
        ('CSE','CSE'),
        ('IT','IT'),
        ('ECE','ECE'),
        ('MEC','MEC'),
        ('CIVL','CIVL')
    ]
    name=models.CharField(max_length=100,null=False)
    roll_number=models.CharField(max_length=14,unique=True)
    email=models.EmailField(null=True,blank=True)
    course=models.CharField(choices=Courses,null=False,max_length=10)
    phone=models.CharField(null=True,blank=True,max_length=10)
    address=models.TextField(null=True,blank=True)
    created_at=models.DateField(null=True,blank=True,auto_now_add=True)
    updated_at=models.DateField(null=True,blank=True,auto_now=True)
    image=models.ImageField(null=True,blank=True,upload_to='student_profile')

    def __str__(self):
        return f"{self.name}"

class Notification(models.Model):

    title = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
class Videos(models.Model):
    name=models.CharField(max_length=200)
    video=models.FileField(upload_to='student_profile/video')