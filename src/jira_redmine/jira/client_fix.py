# coding: utf-8
import json

from jira.client import JIRA
from jira.resources import Project
from jira.utils import json_loads


def create_project(self, key=None, name=None, description=None, assignee=None):
    """Фикс метода создания проекта в клиете Jira."""
    payload = json.dumps({
        'key': key,
        'name': name,
        'projectTypeKey': 'software',
        'projectTemplateKey': (
            'com.pyxis.greenhopper.jira:gh-simplified-scrum-classic'
        ),
        'description': description,
        'leadAccountId': assignee,
        'assigneeType': 'UNASSIGNED',  # PROJECT_LEAD
    })

    url = self._get_url('project')

    r = self._session.post(url, data=payload)
    r.raise_for_status()
    r_json = json_loads(r)
    return Project(self._options, self._session, raw=r_json)


JIRA.create_project = create_project
