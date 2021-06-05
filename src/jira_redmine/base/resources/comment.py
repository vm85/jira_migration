# coding: utf-8
from jira_redmine.base.resources.base import BaseResource
from jira_redmine.base.resources.user import User


class Comment(BaseResource):
    """Ресурс комментария."""

    _CAPTION: str = 'комментарий'

    def __init__(
        self,
        resource_id=None,
        notes=None,
        private_notes=None,
        user=None,
        **kwargs
    ):
        super().__init__(**kwargs)
