# coding: utf-8
from redminelib import Redmine

from jira_redmine.redmine.managers.issue import IssueManager
from jira_redmine.redmine.managers.project import ProjectManager
from jira_redmine.base.repository import BaseRepository


class RedmineRepository(BaseRepository):
    """"""

    _BASE_CLIENT = Redmine
    _PROJECT_MANAGER = ProjectManager
    _ISSUE_MANAGER = IssueManager
