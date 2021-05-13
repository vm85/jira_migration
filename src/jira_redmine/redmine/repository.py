# coding: utf-8
from redminelib import Redmine

from jira_redmine.base.repository import BaseRepository
from jira_redmine.redmine.managers.issue import IssueManager
from jira_redmine.redmine.managers.issue_status import IssueStatusManager
from jira_redmine.redmine.managers.issue_type import IssueTypeManager
from jira_redmine.redmine.managers.project import ProjectManager
from jira_redmine.redmine.managers.user import UserManager


class RedmineRepository(BaseRepository):
    """Репозиторий доступа к данным Redmine."""

    _BASE_CLIENT = Redmine
    _USER_MANAGER = UserManager
    _PROJECT_MANAGER = ProjectManager
    _ISSUE_MANAGER = IssueManager
    _ISSUE_TYPE_MANAGER = IssueTypeManager
    _ISSUE_STATUS_MANAGER = IssueStatusManager
