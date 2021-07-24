from django.db import models
#import pillow
# Create your models here.
class Student(models.Model):
    studentname = models.CharField(max_length=32)
    studentid=models.CharField(max_length=32)
    Class= models.CharField(max_length=32)
    account=models.DecimalField(max_digits=6,decimal_places=2,null=True)
    image=models.ImageField(null=True)

    def __str__(self):
        return '{},{}'.format(self.studentid,self.studentname)