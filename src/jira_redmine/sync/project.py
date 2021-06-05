# coding: utf-8
from typing import Optional
from typing import Dict
from typing import List
from jira_redmine.sync.base import BaseSynchronizer
from jira_redmine.base.resources.project import Project


class ProjectSynchronizer(BaseSynchronizer):
    """Класс синхронизации проектов."""

    def _sync_projects(
        self, specified: List, mapper: Dict
    ) -> Dict[Project, List[Project]]:
        """Синхронизация проектов."""

        if specified:
            projects = []
            for project_key in specified:
                projects.append(self._source.project.get(project_key))
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
        return self._sync_projects(specified, mapper)
