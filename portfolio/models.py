from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
from sympy import true
import datetime

type_proyect = [(1, 'Pagina'),
                (2, 'App')
                ]
class Project(models.Model):
    title = CharField(max_length=100)
    descripttion = CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True) 
    type_proyect = models.IntegerField(
        null=True, choices=type_proyect
    )
    date = models.DateField(null=True)
    
class Profile(models.Model):
    first_name = CharField(max_length=20)
    last_name = CharField(max_length=20)
    profession = CharField(max_length=255)
    phone_number= CharField(max_length=20)
    photo = ImageField(null=True, upload_to='portfolio/profile/')
    favicon = ImageField(null=True, upload_to='portfolio/profile/favicon/')
    descripttion_name = CharField(null=True,max_length=3000) 
    github = URLField(blank=True) 
    linkedin = URLField(blank=True) 
    cv_english = models.FileField(null=True, upload_to = "portfolio/cv/english/")
    cv_spanish= models.FileField(null=True, upload_to = "portfolio/cv/spanis/")
    cv_french= models.FileField(null=True, upload_to = "portfolio/cv/french/")
    descripttion_app= CharField(max_length=3000)
    descripttion_web = CharField(max_length=3000)



class Icon(models.Model):
    icon = ImageField(null=True, upload_to='portfolio/icon/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="icons")
    
class Skill(models.Model):
    skill = ImageField(null=True, upload_to='portfolio/skills/')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="skills")

class Flag(models.Model):
    flag = ImageField(null=True, upload_to='portfolio/flags/')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="flags")
    