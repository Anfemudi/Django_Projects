##import project settings
from django.conf import settings


COPYRIGHT = 'RIG'
COPYLEFT= 'LEF'
CREATIVE_COMMONS = 'CC'

DEFAULT_LICENSES= ( (COPYRIGHT, 'Copyright'),
(COPYLEFT, 'Copyleft'),
(CREATIVE_COMMONS, 'Creative Commons')
)


## GETTATTR SEARCH ON SETTINGS OBJECT THE LICENCES ATTRIBUTE
## IF LICENCES NOT THERE IT WILL PLACE THE DEFAULT_LICENCES AS VALUE.
LICENSES= getattr(settings,'LICENSES',DEFAULT_LICENSES)

BADWORDS = getattr(settings,'PROJECT_BADWORDS',[])