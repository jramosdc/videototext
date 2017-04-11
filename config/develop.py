# ~#~ coding: UTF-8 ~#~

u"""
En este módulo se definen las variables de configuración a ser usadas durante
el desarrollo del sistema. Cada instancia de este repositorio debe definir su
propia configuración en el archivo `instance/config.py`
"""

# Modules ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import logging
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Configuration variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Flask ++++++++++++++++++++++++++++++++
DEBUG = True

LOGGER_HANDLER = logging.StreamHandler()
LOGGER_HANDLER.setLevel(logging.INFO)

TESTING = True
# ++++++++++++++++++++++++++++++++++++++
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
