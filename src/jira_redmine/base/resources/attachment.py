# coding: utf-8
from jira_redmine.base.resources.base import BaseResource
from jira_redmine.base.resources.user import User


class Attachment(BaseResource):
    """Ресурс вложения."""

    _CAPTION: str = 'вложение'

    def __init__(
        self,
        filename: str = None,
        link: str = None,
        description: str = None,
        content_type: str = None,
        creator: User = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.filename = filename
        self.link = link
        self.description = description
        self.content_type = content_type
        self.creator = creator
