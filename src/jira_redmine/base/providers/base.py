# coding: utf-8
from abc import ABCMeta
from abc import abstractmethod
from jira_redmine.base.common import SingletonMeta


class SingletonABCMeta(ABCMeta, SingletonMeta):
    """"""


class BaseProvider(metaclass=SingletonABCMeta):
    """"""

    def __init__(self, *args, **kwargs):
        self._params = kwargs

    @abstractmethod
    def all(self, *args, **kwargs):
        """"""

    @abstractmethod
    def one(self, *args, **kwargs):
        """"""

    @abstractmethod
    def exists(self, *args, **kwargs):
        """"""

    @abstractmethod
    def add(self, *args, **kwargs):
        """"""

    @abstractmethod
    def update(self, *args, **kwargs):
        """"""
