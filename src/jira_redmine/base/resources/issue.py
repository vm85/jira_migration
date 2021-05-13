# coding: utf-8
from jira_redmine.base.resources.base import BaseResource
from jira_redmine.base.resources.issue_status import IssueStatus
from jira_redmine.base.resources.issue_type import IssueType
from jira_redmine.base.resources.project import Project
from jira_redmine.base.resources.user import User
from jira_redmine.base.resources.user import UserDefaultMixin


class Issue(UserDefaultMixin, BaseResource):
    """Ресурс задачи."""

    _CAPTION: str = 'задача'

    def __init__(
        self,
        subject: str = None,
        description: str = None,
        project: Project = None,
        created: str = None,
        creator: User = None,
        issue_type: IssueType = None,
        status: IssueStatus = None,
        assignee: User = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.subject = subject
        self.description = description
        self.project = project
        self.created = created
        self.creator = creator or self.def_user
        self.issue_type = issue_type
        self.status = status
        self.assignee = assignee
