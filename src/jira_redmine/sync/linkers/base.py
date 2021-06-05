# coding: utf-8
from typing import Type
from jira_redmine.base.providers.base import BaseProvider


class BaseLinker:
    """"""

    _provider_class: Type[BaseProvider] = None

    def __init__(self, *args, **kwargs):
        self._provider = self._provider_class(*args, **kwargs)

    def get(self, *args, **kwargs):
        """"""
        return self._provider.one(*args, **kwargs)

    def link(self, *args, **kwargs):
        """"""
        if self._provider.exists(*args, **kwargs):
            self._provider.update(*args, **kwargs)
        else:
            self._provider.add(*args, **kwargs)
