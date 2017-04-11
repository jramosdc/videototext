# ~#~ coding: UTF-8 ~#~

u"""
En este módulo se definen las variables de configuración a ser usadas por
defecto. Cada instancia de este repositorio debe definir su propia
configuración en el archivo `instance/config.py`
"""

# Modules ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Configuration variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Flask ++++++++++++++++++++++++++++++++
DEBUG = False

SECRET_KEY = '837d1fb1e1afe0fa5ac306fd718b725bd8f12e45'
# ++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++
TEMP_DIRECTORY = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'temp'
)
# ++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++
CELERY_BROKER_URL = 'redis://localhost:6379/0'

CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# ++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++++++++++++
WATSON_USER = '25ce03dd-7fbe-4b9e-8f3f-29a434ed9fe9'

WATSON_PASSWORD = 'QxdU3aIayU7X'

WATSON_URL = (
    'https://stream.watsonplatform.net/speech-to-text/'
    'api/v1/recognize?continuous=true&model='
)
# ++++++++++++++++++++++++++++++++++++++
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
