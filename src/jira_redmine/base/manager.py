# coding: utf-8
from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Union
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from jira import JIRA
    from redminelib import Redmine

from jira_redmine.base.resources.base import BaseResource


class BaseManager(ABC):
    """"""

    def __init__(self, client: Union['JIRA', 'Redmine']):
        self._client = client

    @abstractmethod
    def all(self, *args) -> List[BaseResource]:
        """"""

    @abstractmethod
    def get(self, project_id: Union[int, str]) -> BaseResource:
        """"""
