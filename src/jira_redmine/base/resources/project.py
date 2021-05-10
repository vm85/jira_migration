# coding: utf-8
from jira_redmine.base.resources.base import BaseResource


class Project(BaseResource):
    """"""

    def __init__(self, name: str = None, description: str = None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
