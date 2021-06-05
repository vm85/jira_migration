# coding: utf-8
from typing import Dict
from typing import List
from typing import Optional

from jira_redmine.base.resources.attachment import Attachment
from jira_redmine.base.resources.base import BaseResource
from jira_redmine.base.resources.comment import Comment
from jira_redmine.base.resources.issue_status import IssueStatus
from jira_redmine.base.resources.issue_type import IssueType
from jira_redmine.base.resources.journal import Journal
from jira_redmine.base.resources.project import Project
from jira_redmine.base.resources.relation import Relation
from jira_redmine.base.resources.time_entry import TimeEntry
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
        custom_fields: Optional[Dict] = None,
        attachments: Optional[List[Attachment]] = None,
        relations: Optional[List[Relation]] = None,
        comments: Optional[List[Comment]] = None,
        journals: Optional[List[Journal]] = None,
        time_entries: Optional[List[TimeEntry]] = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.subject = subject
        self.description = description
        self.project = project
        self.created = created
        self.creator = creator or self._get_def_user()
        self.issue_type = issue_type
        self.status = status
        self.assignee = assignee
        self.custom_fields = custom_fields
        self.attachments = attachments or []
        self.relations = relations or []
        self.comments = comments or []
        self.journals = journals or []
        self.time_entries = time_entries or []
