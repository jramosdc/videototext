# ~#~ coding: UTF-8 ~#~

# Modules ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import functools
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class SingletonMetaClass(type):
    u"""Implement the singleton pattern in the associated classes.

    Note: the classes affected by this metaclass shouldn't be use in place of
    their base class by any circunstancies.
    """

    def __init__(cls, name, bases, dictionary):
        super(SingletonMetaClass, cls).__init__(name, bases, dictionary)

        @functools.wraps(cls.__init__)
        def not_implemented_init_method(self, *args, **kwargs):
            raise NotImplementedError(
                u"Singletons must be accessed through `get_instance()`"
            )

        cls.__init__, cls.__init = not_implemented_init_method, cls.__init__
        cls.__instance = None
        cls.get_instance = classmethod(SingletonMetaClass.__get_instance)

    @staticmethod
    def __get_instance(cls, *args, **kwargs):
        if not cls.__instance:
            SingletonMetaClass.__swap_init_methods(cls)
            cls.__instance = cls(*args, **kwargs)
            SingletonMetaClass.__swap_init_methods(cls)

        return cls.__instance

    @staticmethod
    def __swap_init_methods(cls):
        cls.__init__, cls.__init = cls.__init, cls.__init__
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
