# coding: utf-8
from typing import List
from typing import Union

from jira_redmine.base.manager import BaseManager
from jira_redmine.base.resources.project import Project


class ProjectManager(BaseManager):
    """"""

    @staticmethod
    def _get_project(project):
        """"""
        return Project(
            resource_id=project.id,
            key=project.identifier,
            name=project.name,
            description=project.description,
        )

    def all(self) -> List[Project]:
        """"""
        projects = self._client.project.all()
        return [self._get_project(project) for project in projects]

    def get(self, project_id: Union[int, str]) -> Project:
        """"""
        project = self._client.project.get(project_id)
        return self._get_project(project)
