from django.contrib.auth.models import User
from django.db import models
from photos.settings import LICENSES
from photos.validators import badwords_detector

# Create your models here.
PUBLIC='PUB'
PRIVATE='PRI'

VISIBILITY= ( (PUBLIC,'Public'),
(PRIVATE,'Private')
)


class Photo(models.Model):

    owner=models.ForeignKey(User,on_delete=models.SET(1))
    name= models.CharField(max_length=150)
    url = models.URLField()
    description= models.TextField(blank=True,null=True, default="",validators=[badwords_detector])
    created_at= models.DateTimeField(auto_now_add=True)
    modified_at= models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3, choices=LICENSES)
    visibility= models.CharField(max_length=3,choices=VISIBILITY,default=PUBLIC)

    def __str__(self): # Campo que se va a visualizar como nombre del elemento
        return self.name



