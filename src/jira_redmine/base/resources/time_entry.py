# coding: utf-8
from jira_redmine.base.resources.base import BaseResource


class TimeEntry(BaseResource):
    """Ресурс трудозатрат."""

    _CAPTION: str = 'трудозатраты'

    def __init__(
        self,
        **kwargs
    ):
        super().__init__(**kwargs)
