# coding: utf-8
from typing import Dict
from typing import List
from typing import Optional

from jira_redmine.base.resources.project import Project
from jira_redmine.sync.base import SynchronizerBase
from jira_redmine.sync.base import SynchronizerCreateMixin


class SynchronizerProject(SynchronizerCreateMixin, SynchronizerBase):
    """Класс синхронизации проектов."""

    def _sync(
        self, specified: List, mapper: Dict
    ) -> Dict[Project, List[Project]]:
        """Синхронизация проектов."""
        if specified:
            projects = [self._source.project.get(key) for key in specified]
        else:
            projects = self._source.project.get_all()

        projects_mapped = {p: [] for p in projects if p.key in mapper}

        for project in projects_mapped:
            # Маппим проекты, для правильного создания задач
            sub_projects = list(filter(
                lambda p: p.key in mapper[project.key],
                projects
            ))
            projects_mapped[project] += sub_projects
            self._get_or_create(self._target.project, project)

        return projects_mapped

    def sync(
        self,
        specified: Optional[List] = None,
        mapper: Optional[Dict] = None
    ) -> Dict[Project, List[Project]]:
        """Основной метод синхронизации."""
        return self._sync(specified, mapper)
