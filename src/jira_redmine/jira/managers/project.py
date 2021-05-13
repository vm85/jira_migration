# coding: utf-8
from typing import List
from typing import Union

from jira_redmine.base.resources.project import Project
from jira_redmine.jira.converter import Converter
from jira_redmine.jira.managers.base import BaseJiraManager


class ProjectManager(BaseJiraManager):
    """Менеджер доступа к проектам Jira."""

    def get_all(self) -> List[Project]:
        """Получить все проекты."""
        projects = self._client.projects()
        return [Converter.get_project(project) for project in projects]

    def get(self, project_id: Union[int, str]) -> Project:
        """Получить проект по идентификатору."""
        project = self._get_or_raise('project', project_id, Project)
        return Converter.get_project(project)

    def create(self, project: Project) -> Project:
        """Создать новый проект."""
        jira_project = self._client.create_project(
            key=project.key,
            name=project.name,
            description=project.description,
            assignee=project.creator.key,
        )
        return self.get(jira_project.key)
