#!/usr/bin/env python
# ~#~ coding: UTF-8 ~#~

u"""
Ejecuta una copia de la aplicación definida en el paquete `audio`. Este script
invoca un servidor de desarrollo y por lo tanto no será usado en producción.
"""

# Modules ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import argparse

from audio import app
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def build_command_line_interface_parser():
    u"""Construye el analizador para la interfaz de línea de comandos."""

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '-H',
        '--host',
        default='127.0.0.1',
        help=u'Dirección del servidor de desarrollo'
    )

    parser.add_argument(
        '-P',
        '--port',
        type=int,
        default='5000',
        help=u'Puerto del servidor de desarrollo'
    )

    return parser
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Main ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    # Obtener los argumentos suministrados por línea de comandos
    args = build_command_line_interface_parser().parse_args()

    # Asociar a la aplicación el manejador de registros de eventos
    if 'LOGGER_HANDLER' in app.config:
        app.logger.addHandler(app.config['LOGGER_HANDLER'])

    # Levantar el servidor de desarrollo
    app.run(host=args.host, port=args.port)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
