# coding: utf-8
from jira import JIRA

from jira_redmine.base.repository import BaseRepository
from jira_redmine.jira.managers.issue import IssueManager
from jira_redmine.jira.managers.issue_status import IssueStatusManager
from jira_redmine.jira.managers.issue_type import IssueTypeManager
from jira_redmine.jira.managers.project import ProjectManager
from jira_redmine.jira.managers.user import UserManager


class JiraRepository(BaseRepository):
    """Репозиторий доступа к данным Jira."""

    _BASE_CLIENT = JIRA
    _USER_MANAGER = UserManager
    _PROJECT_MANAGER = ProjectManager
    _ISSUE_MANAGER = IssueManager
    _ISSUE_TYPE_MANAGER = IssueTypeManager
    _ISSUE_STATUS_MANAGER = IssueStatusManager
