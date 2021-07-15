# coding: utf-8
from abc import ABC
from abc import abstractmethod
from typing import Callable
from typing import List
from typing import Optional
from typing import Type
from typing import Union

from jira import JIRA
from jira.resources import Resource as JiraResource
from redminelib import Redmine
from redminelib.resources.base import BaseResource as RedmineResource

from jira_redmine.base.exceptions import ObjectNotExists
from jira_redmine.base.resources.attachment import Attachment
from jira_redmine.base.resources.base import BaseResource
from jira_redmine.base.resources.issue import Issue


class BaseManager(ABC):
    """Базовый менеджер доступа к данным."""

    def __init__(self, client: Union[JIRA, Redmine]):
        self._client = client

    @abstractmethod
    def get_all(self, *args) -> List[BaseResource]:
        """Получить все или по условию объекты."""

    def _get_or_raise(
        self,
        manager_name: str,
        resource_id: Union[int, str],
        resource_class: Type[BaseResource],
        exceptions: Union[List[Exception], Type[Exception]] = None,
        obj_not_exists_checker: Optional[Callable] = None,
        **kwargs
    ) -> [JiraResource, RedmineResource]:
        """Получить ресурс или выдать ошибку отсутствия ресурса на клиенте."""
        try:
            manager = getattr(self._client, manager_name)
            manager_method = kwargs.get('manager_method')

            if isinstance(exceptions, Exception):
                exceptions = [exceptions]

            method = (
                getattr(manager, manager_method, None)
                if manager_method else manager
            )

            return method(resource_id)
        except exceptions as exc:
            obj_not_exists = (
                obj_not_exists_checker(exc)
                if obj_not_exists_checker else True
            )

            if obj_not_exists:
                raise ObjectNotExists(
                    resource_class.get_resource_caption(),
                    resource_id,
                    str(exc)
                )

            raise exc

    @abstractmethod
    def get(self, resource_id: Union[int, str]) -> BaseResource:
        """Получить один объект."""

    @abstractmethod
    def create(self, resource: BaseResource) -> BaseResource:
        """Создать объект."""


class IssueManagerMixin(ABC):
    """"""

    @abstractmethod
    def add_attachment(self, issue: Issue, attachment: Attachment):
        """"""
