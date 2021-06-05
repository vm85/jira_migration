# coding: utf-8
from typing import Optional

from redminelib.resources import Issue as RedmineIssue
from redminelib.resources import IssueStatus as RedmineIssueStatus
from redminelib.resources import Project as RedmineProject
from redminelib.resources import Tracker as RedmineIssueType
from redminelib.resources import IssueJournal as RedmineComment
from redminelib.resources import IssueRelation as RedmineRelation
from redminelib.resources import TimeEntry as RedmineTimeEntry
from redminelib.resources import User as RedmineUser
from redminelib.resources import Attachment as RedmineAttachment

from jira_redmine.base.converter import BaseConverter
from jira_redmine.base.resources.issue import Issue
from jira_redmine.base.resources.attachment import Attachment
from jira_redmine.base.resources.relation import Relation
from jira_redmine.base.resources.time_entry import TimeEntry
from jira_redmine.base.resources.comment import Comment
from jira_redmine.base.resources.issue_status import IssueStatus
from jira_redmine.base.resources.issue_type import IssueType
from jira_redmine.base.resources.project import Project
from jira_redmine.base.resources.user import User
from jira_redmine.settings import redmine as redmine_params


class Converter(BaseConverter):
    """Класс-преобразователь из ресурса Redmine в локальный ресурс."""

    @classmethod
    def get_user(cls, user: Optional[RedmineUser]) -> Optional[User]:
        """Преобразование пользователя Redmine в локального пользователя."""
        if not user:
            return

        name = getattr(user, 'name', None)
        full_name = ' '.join([
            getattr(user, 'firstname', ''),
            getattr(user, 'lastname', '')
        ])
        return User(
            resource_id=str(user.id),
            name=name or full_name,
            # TODO нет поля
            email=getattr(user, 'email', None) or getattr(user, 'mail', None)
        )

    @classmethod
    def get_issue_status(cls, status: RedmineIssueStatus) -> IssueStatus:
        """Преобразование статуса задачс Redmine в локальный статус задачи."""
        # TODO status mapper
        return IssueStatus(
            resource_id=str(status.id),
            name=status.name,
        )

    @classmethod
    def get_issue_type(cls, issue_type: RedmineIssueType) -> IssueType:
        """Преобразование типа задачи Redmine в локальный тип задачи."""
        # TODO mapper
        return IssueType(
            resource_id=str(issue_type.id),
            name=issue_type.name,
        )

    @classmethod
    def get_project(cls, project: RedmineProject) -> Project:
        """Преобразование проекта Redmine в локальный проект."""
        # TODO разобраться почему нет полей
        return Project(
            resource_id=str(project.id),
            key=str(getattr(project, 'identifier', '')),
            name=project.name,
            description=getattr(project, 'description', ''),
            creator=None,  # TODO
        )

    @classmethod
    def get_issue(cls, issue: RedmineIssue) -> Issue:
        """Преобразование задачи Redmine в локальную задачу."""
        project = issue.project

        custom_fields_names = redmine_params['issue']['custom_fields']
        custom_fields = {}
        for custom_field_name in custom_fields_names:
            custom_field_obj = next(filter(
                lambda f: f.name == custom_field_name,
                issue.custom_fields
            ), None)
            custom_fields[custom_field_name] = (
                getattr(custom_field_obj, 'value', None)
            )

        return Issue(
            resource_id=str(issue.id),
            subject=issue.subject,
            description=issue.description,
            project=cls.get_project(project),
            created=issue.created_on,
            creator=cls.get_user(issue.author),
            issue_type=cls.get_issue_type(issue.tracker),
            status=cls.get_issue_status(issue.status),
            assignee=cls.get_user(getattr(issue, 'assigned_to', None)),
            custom_fields=custom_fields,
            attachments=[
                cls.get_attachment(attachment)
                for attachment in issue.attachments
                if attachment
            ],
            # relations=[
            #     cls.get_relation(relation)
            #     for relation in issue.relations
            #     if relation
            # ],
            # comments=[
            #     cls.get_comment(journal)
            #     for journal in issue.journals
            # ],
            # journals=[
            #     cls.get_journal(journal)
            #     for journal in issue.journals
            # ],
            # time_entries=[
            #     cls.get_time_entry(time_entry)
            #     for time_entry in issue.time_entries
            # ],
        )

    @classmethod
    def get_attachment(
        cls, attachment: Optional[RedmineAttachment]
    ) -> Optional[Attachment]:
        """Преобразование вложения Redmine в локальное вложение."""
        if not attachment:
            return

        return Attachment(
            resource_id=str(attachment.id),
            filename=attachment.filename,
            link=attachment.content_url,
            description=attachment.description,
            content_type=attachment.content_type,
            creator=cls.get_user(attachment.author),
        )

    @classmethod
    def get_relation(
        cls, relation: Optional[RedmineRelation]
    ) -> Optional[Relation]:
        """Преобразование связи задач Redmine в локальную связь задач."""
        if not relation:
            return

        return Relation(
            resource_id=str(relation.id),
            issue_id=relation.issue_id,
            issue_to_id=relation.issue_to_id,
            relation_type=relation.relation_type,
        )

    @classmethod
    def get_comment(
        cls, comment: Optional[RedmineComment]
    ) -> Optional[Comment]:
        """Преобразование комментария Redmine в локальный комментарий."""
        if not comment or not getattr(comment, 'notes', None):
            return

        return Comment(
            resource_id=str(comment.id),
            notes=comment.notes,
            private_notes=comment.private_notes,
            user=cls.get_user(comment.user),
        )

    @classmethod
    def get_time_entry(
        cls, time_entry: Optional[RedmineTimeEntry]
    ) -> Optional[TimeEntry]:
        """Преобразование учета часов Redmine в локальный учет часов."""
        if not time_entry:
            return

        return TimeEntry(
            resource_id=str(time_entry.id),
            # activity=cls.get_activity('id', 'name'),
            comments=time_entry.comments,
            created_on=time_entry.created_on,
            hours=time_entry.hours,
            spent_on=time_entry.spent_on,
            user=cls.get_user(time_entry.user),
        )
