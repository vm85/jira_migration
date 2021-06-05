# coding: utf-8


class BaseRepository:
    """Базовый репозиторий доступа к данным."""

    # Клиент доступа к данным
    _BASE_CLIENT = None
    # Менеджер доступа к пользователям
    _USER_MANAGER = None
    # Менеджер доступа к проетам
    _PROJECT_MANAGER = None
    # Менеджер доступа к задачим
    _ISSUE_MANAGER = None
    # Менеджер доступа к типам задач
    _ISSUE_TYPE_MANAGER = None
    # Менеджер доступа к статусам задач
    _ISSUE_STATUS_MANAGER = None

    def __init__(self, *args, **kwargs):
        self._client = self._BASE_CLIENT(*args, **kwargs)
        self.user = self._USER_MANAGER(self._client)
        self.project = self._PROJECT_MANAGER(self._client)
        self.issue = self._ISSUE_MANAGER(self._client)
        self.issue_type = self._ISSUE_TYPE_MANAGER(self._client)
        self.issue_status = self._ISSUE_STATUS_MANAGER(self._client)

    def __str__(self):
        return self.__doc__
