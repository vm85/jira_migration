# coding: utf-8
from typing import Optional

from jira.resources import Attachment as JiraAttachment
from jira.resources import Issue as JiraIssue
from jira.resources import IssueType as JiraIssueType
from jira.resources import Project as JiraProject
from jira.resources import Status as JiraIssueStatus
from jira.resources import User as JiraUser

from jira_redmine.base.converter import BaseConverter
from jira_redmine.base.resources.issue import Attachment
from jira_redmine.base.resources.issue import Issue
from jira_redmine.base.resources.issue_status import IssueStatus
from jira_redmine.base.resources.issue_type import IssueType
from jira_redmine.base.resources.project import Project
from jira_redmine.base.resources.user import User


class Converter(BaseConverter):
    """Класс-преобразователь из ресурса Jira в локальный ресурс."""

    @classmethod
    def get_user(cls, user: Optional[JiraUser]) -> Optional[User]:
        """Преобразование пользователя Jira в локального пользователя."""
        if not user:
            return

        return User(
            resource_id=str(user.accountId),
            name=user.displayName,
            # TODO empty some times
            email=getattr(user, 'emailAddress', None),
        )

    @classmethod
    def get_issue_status(cls, status: JiraIssueStatus) -> IssueStatus:
        """Преобразование статуса задачс Jira в локальный статус задачи."""
        # TODO status mapper
        return IssueStatus(
            resource_id=str(status.id),
            name=status.name,
        )

    @classmethod
    def get_issue_type(cls, issue_type: JiraIssueType) -> IssueType:
        """Преобразование типа задачи Jira в локальный тип задачи."""
        # TODO mapper
        return IssueType(
            resource_id=str(issue_type.id),
            name=issue_type.name,
            description=getattr(issue_type, 'description', None),
        )

    @classmethod
    def get_project(cls, project: JiraProject) -> Project:
        """Преобразование проекта Jira в локальный проект."""
        return Project(
            resource_id=str(project.id),
            key=str(project.key),
            name=project.name,
            # TODO разобраться почему нет описания в all
            description=getattr(project, 'description', None),
            creator=cls.get_user(getattr(project, 'lead', None))
        )

    @classmethod
    def get_issue(cls, issue: JiraIssue) -> Issue:
        """Преобразование задачи Jira в локальную задачу."""
        project = issue.fields.project
        return Issue(
            resource_id=str(issue.id),
            subject=issue.fields.summary,
            description=issue.fields.description,
            project=cls.get_project(project),
            created=issue.fields.created,
            creator=cls.get_user(issue.fields.creator),
            issue_type=cls.get_issue_type(issue.fields.issuetype),
            status=cls.get_issue_status(issue.fields.status),
            assignee=cls.get_user(issue.fields.assignee),
            story_points=issue.fields.story_points,
            attachments=[
                cls.get_attachment(attachment)
                for attachment in issue.fields.attachment
                if attachment
            ],
        )

    @classmethod
    def get_attachment(
        cls, attachment: Optional[JiraAttachment]
    ) -> Optional[Attachment]:
        """Преобразование вложения Jira в локальное вложение."""
        if not attachment:
            return

        return Attachment(
            resource_id=str(attachment.id),
            name=attachment.name,
            filename=attachment.filename,
            link=attachment.content,
            content_type=attachment.content_type,
            creator=cls.get_user(attachment.author),
        )
