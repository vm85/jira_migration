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
    issue=dict(
        custom_fields=json.loads(os.getenv('JIRA_ISSUE_CUSTOM_FIELDS', '[]')),
    ),
)

redmine = dict(
    url=os.getenv('REDMINE_URL', ''),
    user=os.getenv('REDMINE_USER', ''),
    password=os.getenv('REDMINE_PASS', ''),
    issue=dict(
        custom_fields=json.loads(
            os.getenv('REDMINE_ISSUE_CUSTOM_FIELDS', '[]')
        ),
    ),
)

project = dict(
    specified=json.loads(os.getenv('PROJECTS_SPECIFIED', '[]')),
    mapper=json.loads(os.getenv('PROJECTS_MAPPER', '{}')),
)

db = dict(
    driver=os.getenv('DATABASE_DRIVER', ''),
    server=os.getenv('DATABASE_SERVER', ''),
    db_name=os.getenv('DATABASE_NAME', ''),
    params=json.loads(os.getenv('DATABASE_ADDITIONAL', '{}')),
    link_params=dict(
        table_name=os.getenv('LINK_TABLE_NAME', 'jira_redmine_link'),
        resource_field_name=os.getenv('LINK_RESOURCE_FIELD', 'resource'),
        source_field_name=os.getenv('LINK_SOURCE_FIELD', 'redmine_key'),
        target_field_name=os.getenv('LINK_TARGET_FIELD', 'jira_key'),
    ),
)
