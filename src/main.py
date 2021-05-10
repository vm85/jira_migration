# coding: utf-8
from pprint import pprint

from jira_redmine import settings
from jira_redmine.jira.repository import JiraRepository
from jira_redmine.redmine.repository import RedmineRepository


print('*' * 20, ' JIRA ', '*' * 20)
jira_repo = JiraRepository(
    server=settings.jira['url'],
    basic_auth=(
        settings.jira['user'],
        settings.jira['password']
    )
)
projects = jira_repo.project.all()
print('Проекты:')
pprint(projects)

print()
print('1 проект:')
project = jira_repo.project.get('PD')
print(project)

print()
print('Таски:')
issues = jira_repo.issue.all('PD')
print(issues)

print()
print('1 таска:')
issue = jira_repo.issue.get('PD-1')
print(issue)

print()
print('*' * 20, ' Redmine ', '*' * 20)
redmine_repo = RedmineRepository(
    settings.redmine['url'],
    username=settings.redmine['user'],
    password=settings.redmine['password']
)

print()
print('Проекты:')
projects = redmine_repo.project.all()
print(list(projects))

print()
print('1 проект:')
project = redmine_repo.project.get('prodact')
print(project)

print()
print('Таски:')
issues = redmine_repo.issue.all('prodact')
print(list(issues))

print()
print('1 таска:')
issue = redmine_repo.issue.get(4385)
print(issue)
