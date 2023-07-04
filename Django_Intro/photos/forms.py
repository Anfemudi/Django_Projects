from django import forms
from photos.models import Photo
from photos.settings import BADWORDS
from django.core.exceptions import ValidationError


class PhotoForm(forms.ModelForm):

    """Form for the Photo model """

    class Meta:
        model=Photo
        exclude = ['owner']

    def clean(self):
        """ validates if in the descriptions are words 
        which are not allowed based on settings.BADWORDS
        :return: dict with attributes if ok """

        cleaned_data=super(PhotoForm,self).clean()
        description= cleaned_data.get('description','')
        print("aqui va la descripcion")
        print(description)
        print("aqui termino la descripcion")
        for badword in BADWORDS:
            if badword.lower() in description.lower():
                raise ValidationError('word {0} is not allowed in description'.format(badword))



        ## if everything ok return cleaned data var
        return cleaned_data


## https://w7.pngwing.com/pngs/1008/857/png-transparent-pidgeotto-pidgey-johto-pokemon-shroomish-pokemon-galliformes-chicken-vertebrate.png