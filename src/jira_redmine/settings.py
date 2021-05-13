# coding: utf-8
import json
import os


DEFAULT_USER = dict(
    ID=os.getenv('DEFAULT_USER_ID', ''),
    NAME=os.getenv('DEFAULT_USER_NAME', ''),
)
jira = dict(
    url=os.getenv('JIRA_URL', ''),
    user=os.getenv('JIRA_USER', ''),
    password=os.getenv('JIRA_PASS', ''),
)
redmine = dict(
    url=os.getenv('REDMINE_URL', ''),
    user=os.getenv('REDMINE_USER', ''),
    password=os.getenv('REDMINE_PASS', ''),
)

projects_only = os.getenv('PROJECTS_ONLY', '').split(',')

projects_mapper = json.loads(os.getenv('PROJECTS_MAPPER', '{}'))
