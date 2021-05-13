# coding: utf-8
from jira_redmine import settings
from jira_redmine.jira.repository import JiraRepository
from jira_redmine.redmine.repository import RedmineRepository
from jira_redmine.sync.synchronizer import Synchronizer
import jira_redmine.jira.client_fix  # noqa: F401


redmine_repo = RedmineRepository(
    settings.redmine['url'],
    username=settings.redmine['user'],
    password=settings.redmine['password']
)

jira_repo = JiraRepository(
    server=settings.jira['url'],
    basic_auth=(
        settings.jira['user'],
        settings.jira['password']
    )
)

s = Synchronizer(redmine_repo, jira_repo)
s.sync()
# s.print_all(
#   [[], ['11'], [], ['1'], [], ['1'], [], ['prodact'], ['prodact'], ['4385']],
#   [[], ['123'], [], ['10011'], [], ['3'], [], ['PD'], ['PD'], ['PD-2']],
# )

"""
from jira_redmine.base.resources.issue import Issue
from jira_redmine.base.resources.issue_status import IssueStatus
from jira_redmine.base.resources.issue_type import IssueType
from jira_redmine.base.resources.project import Project
from jira_redmine.base.resources.user import User

creator = User(resource_id='6024811bc47e730068048dae', name='Chen Viktor')
assignee = User(resource_id='5c6e65b45b4c267532743543', name='Маслов Владимир')
issuetype = IssueType(resource_id=10015, name='Баг')
# status = IssueStatus(resource_id=21, name='В работе')
status = IssueStatus(resource_id=0, name='Готово')
project = Project(
    resource_id='123',
    key='PD',
    name='PD'
)
issue = Issue(
    resource_id='PD-12',
    subject='New issue 12',
    description='Look into this one',
    project=project,
    # created='2021-04-30T08:24:44+03:00',
    creator=creator,
    issue_type=issuetype,
    status=status,
    assignee=assignee,
)

res = jira_repo.issue.create(issue)
pprint(res)
# """
