# coding: utf-8
from typing import Dict
from typing import Optional
from jira_redmine.sync.base import BaseSynchronizer
from jira_redmine.sync.project import ProjectSynchronizer
from jira_redmine.sync.issue import IssueSynchronizer


class MainSynchronizer(BaseSynchronizer):
    """Основной класс синхронизации объектов."""

    def __init__(self, *args):
        super().__init__(*args)
        self._projects_sync = ProjectSynchronizer(*args)
        self._issues_sync = IssueSynchronizer(*args)

    def sync(self, project_params: Optional[Dict] = None):
        """Основной метод синхронизации."""
        project_params = project_params or {}
        projects_mapped = self._projects_sync.sync(**project_params)
        self._issues_sync.sync(projects_mapped=projects_mapped)

    def print_all(self, source_args, target_args):
        """For tests."""
        self._print_one(self._source, *source_args)
        self._print_one(self._target, *target_args)

    @staticmethod
    def _print_one(repo, *args):
        """For tests one."""
        print('\n\n', '*' * 20, ' ', repo, ' ', '*' * 20)

        params = [
            ['Пользователи', 'user', 'get_all'],
            ['1 Пользователь', 'user', 'get'],
            ['Типы задач', 'issue_type', 'get_all'],
            ['1 тип задач', 'issue_type', 'get'],
            ['Статусы задач', 'issue_status', 'get_all'],
            ['1 статус  задач', 'issue_status', 'get'],
            ['Проекты', 'project', 'get_all'],
            ['1 проект', 'project', 'get'],
            ['Таски', 'issue', 'get_all'],
            ['1 таска', 'issue', 'get'],
        ]

        params = zip(params, args)

        for (name, manager, method), arg in params:
            try:
                print(f'\n{name}:')
                resource = getattr(getattr(repo, manager), method)(*arg)
                print(resource)
            except Exception as exc:
                print('Exception:', exc)
                # traceback.print_exc(),
                # traceback.print_tb(exc.__traceback__),
                # traceback.print_exception(*sys.exc_info()),
