# coding: utf-8
from jira_redmine.base.resources.base import BaseResource
from jira_redmine.base.resources.user import User


class Journal(BaseResource):
    """Ресурс журнала."""

    _CAPTION: str = 'журнал'

    def __init__(
        self,
        **kwargs
    ):
        super().__init__(**kwargs)
