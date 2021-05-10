# coding: utf-8
import os


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

# projects = dict(
#     productTeam=71,
# ),
