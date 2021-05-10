# coding: utf-8
from jira_redmine.base.resources.base import BaseResource


class Issue(BaseResource):
    """"""

    def __init__(self, subject: str = None, description: str = None, **kwargs):
        super().__init__(**kwargs)
        self.subject = subject
        self.description = description
        self.project = kwargs['project']
