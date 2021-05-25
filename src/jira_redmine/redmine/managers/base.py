# coding: utf-8
from abc import ABC
from typing import Type
from typing import Union

from redminelib.exceptions import ResourceNotFoundError
from redminelib.resources.base import BaseResource as RedmineResource

from jira_redmine.base.manager import BaseManager
from jira_redmine.base.resources.base import BaseResource


class BaseRedmineManager(BaseManager, ABC):
    """Базовый менеджер доступа к данным Redmine."""

    def _get_or_raise(
        self,
        manager_name: str,
        resource_id: Union[int, str],
        resource_class: Type[BaseResource],
        manager_method: str = None,
        **kwargs
    ) -> RedmineResource:
        """Получить ресурс или выдать ошибку отсутствия ресурса на Redmine."""
        return super()._get_or_raise(
            manager_name,
            resource_id,
            resource_class,
            exceptions=ResourceNotFoundError,
            manager_method=manager_method
        )
