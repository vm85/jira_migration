# coding: utf-8


class SingletonMeta(type):
    """Паттерн Одиночка."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Реализация Одиночки."""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
