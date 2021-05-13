# coding: utf-8


class BaseResource:
    """Базовый ресурс."""

    _CAPTION: str = None

    def __init__(self, resource_id: str = None, key: str = None):
        if not self._CAPTION:
            ValueError('Не заполнено свойство класса _CAPTION')

        self.resource_id = resource_id
        self.key = key or resource_id

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.key)

    @classmethod
    def get_resource_caption(cls) -> str:
        """Возвращает человекочитаемое имя ресурса."""
        return cls._CAPTION
