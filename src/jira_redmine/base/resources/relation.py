# coding: utf-8
from jira_redmine.base.resources.base import BaseResource


class Relation(BaseResource):
    """Ресурс связи задач."""

    _CAPTION: str = 'связь задач'

    def __init__(
        self,
        issue_id=None,
        issue_to_id=None,
        relation_type=None,
        **kwargs
    ):
        super().__init__(**kwargs)
