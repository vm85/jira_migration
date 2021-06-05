# coding: utf-8
from abc import ABCMeta
from abc import abstractmethod

from jira_redmine.base.common import SingletonMeta


class SingletonABCMeta(ABCMeta, SingletonMeta):
    """Одиночка для провайдера."""


class BaseProvider(metaclass=SingletonABCMeta):
    """Базовый провайдер работы с данными."""

    def __init__(self, *args, **kwargs):
        self._params = kwargs

    @abstractmethod
    def all(self, *args, **kwargs):  # noqa: A003
        """Получение всех строк."""

    @abstractmethod
    def one(self, *args, **kwargs):
        """Получение одной строки."""

    @abstractmethod
    def exists(self, *args, **kwargs):
        """Проверка на существование данных."""

    @abstractmethod
    def add(self, *args, **kwargs):
        """Создание данных."""

    @abstractmethod
    def update(self, *args, **kwargs):
        """Изменение данных."""
