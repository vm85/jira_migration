# coding: utf-8
from abc import ABC
from abc import abstractmethod
from typing import Type

from jira_redmine.base.providers.base import BaseProvider


class BaseLinker(ABC):
    """Базовый класс для связи ресурсов Jira и Redmine."""

    _provider_class: Type[BaseProvider] = None

    def __init__(self, *args, **kwargs):
        self._provider = self._provider_class(*args, **kwargs)

    def get(self, *args, **kwargs):
        """Получить данные по одиному ресурсу."""
        return self._provider.one(*args, **kwargs)

    @abstractmethod
    def get_target_key(self, *args, **kwargs):
        """Получить код целевого ресурса."""

    def link(self, *args, **kwargs):
        """Связать ресурсы."""
        if self._provider.exists(*args, **kwargs):
            self._provider.update(*args, **kwargs)
        else:
            self._provider.add(*args, **kwargs)
