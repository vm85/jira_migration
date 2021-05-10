# coding: utf-8


class BaseResource:
    """"""

    def __init__(self, **kwargs):
        self.resource_id = kwargs['resource_id']
        self.key = kwargs.get('key', '')

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
