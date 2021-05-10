# coding: utf-8
from jira import JIRA

from jira_redmine.jira.managers.issue import IssueManager
from jira_redmine.jira.managers.project import ProjectManager
from jira_redmine.base.repository import BaseRepository


class JiraRepository(BaseRepository):
    """"""

    _BASE_CLIENT = JIRA
    _PROJECT_MANAGER = ProjectManager
    _ISSUE_MANAGER = IssueManager
