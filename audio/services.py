# ~#~ coding: UTF-8 ~#~

# Modules ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask

from . import utils
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class FlaskService(Flask):
    __metaclass__ = utils.SingletonMetaClass

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("instance_relative_config", True)

        super(FlaskService, self).__init__(*args, **kwargs)

        # Parámetros de configuración por defecto
        self.__load_default_config_file()

        # Parámetros de configuración apuntados por la variable de entorno
        self.__load_envvar_config_file()

        # Parámetros de configuración de la instancia
        self.__load_instance_config_file()

    def __load_default_config_file(self):
        self.config.from_object("config.default")

    def __load_envvar_config_file(self):
        try:
            self.config.from_envvar("APP_CONFIG_FILE")

        except (RuntimeError, IOError):
            pass

        else:
            self.logger.info(u" ".join([
                u"El archivo de configuración apuntado por la variable de",
                u"entorno `APP_CONFIG_FILE` ha sido cargado exitosamente."
            ]))

    def __load_instance_config_file(self):
        try:
            self.config.from_pyfile("config.py")

        except IOError:
            pass

        else:
            self.logger.info(u" ".join([
                u"El archivo de configuración de esta instancia ha sido",
                u"cargado exitosamente."
            ]))
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
