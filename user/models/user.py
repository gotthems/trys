from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from user.choices.choice import MartialStatusChoices, EducationalStatusChoices, ProfessionChoices, GenderChoices



class Interest(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True  )

    def __str__(self):
        return self.name


class User(AbstractUser):
    birthday = models.DateField(null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    gender = models.PositiveIntegerField(null=True,choices=GenderChoices.CHOICES)
    martial_status =  models.PositiveIntegerField(null=True, choices=MartialStatusChoices.CHOICES)
    educational_status = models.PositiveIntegerField(null=True, choices=EducationalStatusChoices.CHOICES)
    profession = models.PositiveIntegerField(null=True, choices=ProfessionChoices.CHOICES)
    interests = models.ManyToManyField(to=Interest,null=True, blank=True)


    class Meta:
        verbose_name= "User"

    @property
    def info(self):
        interests = ", ".join([interest.name for interest in self.interests.all()]) or "-"

        context = {
            'interests': interests,

        }

        return context