# coding: utf-8
from jira_redmine.base.repository import BaseRepository
from jira_redmine.base.exceptions import ObjectNotExists
from jira_redmine.base.resources.base import BaseResource
from abc import abstractmethod
from abc import ABC
from jira_redmine.sync.linkers.base import BaseLinker
from jira_redmine.base.manager import BaseManager


class BaseSynchronizer(ABC):
    """Базовый класс синхронизации объектов."""

    def __init__(
        self, source: BaseRepository, target: BaseRepository, linker: BaseLinker
    ):
        self._source = source
        self._target = target
        self._linker = linker

    @abstractmethod
    def sync(self, **kwargs):
        """"""

    def _get_or_create(self, manager: BaseManager, source_obj: BaseResource):
        """"""
        try:
            target_object = manager.get(source_obj.key)
        except ObjectNotExists:
            target_object = manager.create(source_obj)

        self._linker.link(source_obj, target_object)

        return target_object
