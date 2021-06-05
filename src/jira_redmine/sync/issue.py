# coding: utf-8
from typing import Dict
from typing import List
from typing import Optional

from jira_redmine.base.resources.attachment import Attachment
from jira_redmine.base.resources.comment import Comment
from jira_redmine.base.resources.issue import Issue
from jira_redmine.base.resources.journal import Journal
from jira_redmine.base.resources.project import Project
from jira_redmine.base.resources.relation import Relation
from jira_redmine.base.resources.time_entry import TimeEntry
from jira_redmine.sync.base import BaseSynchronizer


class IssueSynchronizer(BaseSynchronizer):
    """Класс синхронизации задач."""

    def _sync_additional_info(
        self, source_issue: Issue, target_issue: Issue
    ):
        """Синхронизация дополнительных данных задачи."""
        self._sync_attachments(target_issue, source_issue.attachments)
        self._sync_relations(target_issue, source_issue.relations)
        self._sync_comments(target_issue, source_issue.comments)
        self._sync_journals(target_issue, source_issue.journals)
        self._sync_time_entries(target_issue, source_issue.time_entries)

    def _sync_attachments(self, issue: Issue, attachments: List[Attachment]):
        """Синхронизация вложений."""

    def _sync_relations(self, issue: Issue, relations: List[Relation]):
        """Синхронизация связанных задач."""
        # TODO связываемых задач может еще не существовать

    def _sync_comments(self, issue: Issue, comments: List[Comment]):
        """Синхронизация комментариев."""

    def _sync_journals(self, issue: Issue, journals: List[Journal]):
        """Синхронизация истории."""

    def _sync_time_entries(self, issue: Issue, time_entries: List[TimeEntry]):
        """Синхронизация трудозатрат."""

    def _get_issues(
        self, projects_mapped: Dict[Project, List[Project]]
    ) -> List[Issue]:
        """Получить список задач по проекту."""
        # TODO подумать если не передано projects_mapped
        issues = []
        for project, sub_projects in projects_mapped.items():
            issues += self._source.issue.get_all(project.key)
            for sub_project in sub_projects:
                issues += self._source.issue.get_all(sub_project.key)

        return list(sorted(issues, key=lambda x: x.key))

    def _sync(
        self, projects_mapped: Optional[Dict[Project, List[Project]]]
    ):
        """Синхронизация задач."""
        for issue in self._get_issues(projects_mapped):
            target_issue = self._get_or_create(self._target.issue, issue)
            self._sync_additional_info(issue, target_issue)

    def sync(
        self, projects_mapped: Optional[Dict[Project, List[Project]]] = None
    ):
        """Основной метод синхронизации."""
        self._sync(projects_mapped)
