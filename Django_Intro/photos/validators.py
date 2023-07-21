from photos.settings import BADWORDS
from django.core.exceptions import ValidationError


def badwords_detector(value):
    """ validates if in 'value' the descriptions 'are words 
    which are not allowed based on settings.BADWORDS
    :return: Bool"""

    for badword in BADWORDS:
        if badword.lower() in value.lower():
            raise ValidationError('word {0} is not allowed in description'.format(badword))
    
    #if everything OK return True
    return True

    