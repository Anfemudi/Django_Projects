from django import forms
from photos.models import Photo
from photos.settings import BADWORDS
from django.core.exceptions import ValidationError


class PhotoForm(forms.ModelForm):

    """Form for the Photo model """

    class Meta:
        model=Photo
        exclude = ['owner']