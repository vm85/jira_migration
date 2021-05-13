# coding: utf-8
from typing import List
from typing import Union

from jira_redmine.base.resources.project import Project
from jira_redmine.redmine.converter import Converter
from jira_redmine.redmine.managers.base import BaseRedmineManager


class ProjectManager(BaseRedmineManager):
    """Менеджер доступа к проектам Redmine."""

    def get_all(self) -> List[Project]:
        """Получить все проекты."""
        projects = self._client.project.all()
        return [Converter.get_project(project) for project in projects]

    def get(self, project_id: Union[int, str]) -> Project:
        """Получить проект по идентификатору."""
        project = self._get_or_raise(
            'project', project_id, Project, manager_method='get'
        )
        return Converter.get_project(project)

    def create(self, project: Project) -> Project:
        """Создать новый проект."""
        raise NotImplementedError
        # project = self._client.project.create(
        #     # name='Vacation',
        #     # identifier='vacation',
        #     # description='foo',
        #     # homepage='http://foo.bar',
        #     # is_public=True,
        #     # parent_id=345,
        #     # inherit_members=True,
        #     # tracker_ids=[1, 2],
        #     # issue_custom_field_ids=[1, 2],
        #     # custom_fields=[
        #     #     {'id': 1, 'value': 'foo'},
        #     #     {'id': 2, 'value': 'bar'}
        #     # ],
        #    # enabled_module_names=['calendar', 'documents', 'files', 'gantt']
        # )
        # return Converter.get_project(project)
