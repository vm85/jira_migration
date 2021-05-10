# coding: utf-8
from abc import ABC


class BaseRepository(ABC):
    """"""

    #
    _BASE_CLIENT = None
    #
    _PROJECT_MANAGER = None
    #
    _ISSUE_MANAGER = None

    def __init__(self, *args, **kwargs):
        self._client = self._BASE_CLIENT(*args, **kwargs)
        self.project = self._PROJECT_MANAGER(self._client)
        self.issue = self._ISSUE_MANAGER(self._client)
