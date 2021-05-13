# coding: utf-8


class ObjectNotExists(Exception):
    """Ошибка отсутствия ресурса на клиенте."""

    _MESSAGE_TEMPLATE: str = 'Ресурс "%s" с ключом "%s" не существует.\n%s'

    def __init__(self, resource_name: str, key: str, msg: str):
        msg = self._MESSAGE_TEMPLATE % (resource_name.upper(), key, msg)
        super().__init__(msg)
