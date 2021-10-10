from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    branches=(
        ('Cse','Cse'), #right side value shows in drop down menue.. left side value is the value that stores in db
        ('Ece', 'Ece'),
        ('Eee','Eee'),
        ('IS','IS'),
        ('Mechanical','Mechanical'),
        ('Civil','Civil'),
        ('Chemical','Chemical'),
    )
    difficulty=(
        ('Ease','Easy'),
        ('Medium','Medium'),
        ('Hard','Hard'),
    )
    CompanyName = models.CharField(max_length=50)
    Difficulty=models.CharField(max_length=7,choices=difficulty,default='Intermediate')
    department=models.CharField(max_length=20,choices=branches,default='Cse')
    ctc=models.DecimalField(max_digits=5, decimal_places=2)
    Experience = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,

    )
    
    


    def __str__(self):
        return self.CompanyName

