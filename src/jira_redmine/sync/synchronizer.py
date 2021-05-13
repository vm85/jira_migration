# coding: utf-8
from jira_redmine.base.exceptions import ObjectNotExists
from jira_redmine.base.repository import BaseRepository
from jira_redmine.settings import projects_mapper
from jira_redmine.settings import projects_only


class Synchronizer:
    """Класс синхронизации объектов из клиента-источника в целевой-клиент."""

    def __init__(self, source: BaseRepository, target: BaseRepository):
        self._source = source
        self._target = target
        self._projects = {}

    def _sync_projects(self):
        """Синхронизация проектов."""
        projects = self._source.project.get_all()

        if projects_only:
            projects = list(filter(lambda p: p.key in projects_only, projects))

        self._projects = {p: [] for p in projects if p.key in projects_mapper}

        for project in self._projects:
            # Маппим проекты, для правильного создания задач
            sub_projects = list(filter(
                lambda p: p.key in projects_mapper[project.key],
                projects
            ))
            self._projects[project].append(sub_projects)

            try:
                self._target.project.get(project.key)
                # TODO update?
            except ObjectNotExists:
                # Создаем проект
                self._target.project.create(project)
                break

    def _sync_issues(self):
        """Синхронизация задач."""

    def sync(self):
        """Основной метод синхронизации."""
        self._sync_projects()
        self._sync_issues()

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
            print(f'\n{name}:')
            try:
                resource = getattr(getattr(repo, manager), method)(*arg)
                print(resource)
            except Exception as exc:
                print('Exception:', exc)
