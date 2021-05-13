# coding: utf-8


# coding: utf-8
from abc import ABC
from http import HTTPStatus
from typing import Type
from typing import Union

from jira.exceptions import JIRAError
from jira.resources import Resource as JiraResource

from jira_redmine.base.manager import BaseManager
from jira_redmine.base.resources.base import BaseResource


class BaseJiraManager(BaseManager, ABC):
    """Базовый менеджер доступа к данным Jira."""

    def _get_or_raise(
        self,
        manager_name: str,
        resource_id: Union[int, str],
        resource_class: Type[BaseResource],
        **kwargs
    ) -> JiraResource:
        """Получить ресурс или выдать ошибку отсутствия ресурса Jira."""
        return super()._get_or_raise(
            manager_name,
            resource_id,
            resource_class,
            exceptions=JIRAError,
            obj_not_exists_checker=(
                lambda e: e.status_code == HTTPStatus.NOT_FOUND
            ),
        )
