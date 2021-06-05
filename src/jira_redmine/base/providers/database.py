# coding: utf-8
from typing import Optional
from typing import Dict
from typing import Union
from typing import List
import pyodbc
from jira_redmine.base.providers.base import BaseProvider


class DBProvider(BaseProvider):
    """"""

    __connection: pyodbc.Connection = None

    def __init__(
        self, driver: str, server: str, database: str, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self._params.update(dict(
            driver=driver,
            server=server,
            database=database,
        ))

    @property
    def _connection_string(self):
        """"""
        return self._get_assign_str(self._params, ';', True)

    @property
    def _connection(self) -> pyodbc.Connection:
        """"""
        if not self.__connection:
            self.__connection = pyodbc.connect(self._connection_string)

        return self.__connection

    @staticmethod
    def _get_assign_str(
        column_values: Union[Dict, List],
        joiner: str = ',',
        with_values: bool = False
    ):
        """"""
        if isinstance(column_values, list):
            column_values = dict.fromkeys(column_values)

        return joiner.join(map(
            lambda k, v: '='.join(
                [k, str(v)] if with_values
                else [k, '?']
            ),
            column_values.keys(),
            column_values.values(),
        ))

    def _execute(self, sql: str, *args, **_) -> pyodbc.Cursor:
        """"""
        return self._connection.execute(sql, *args)

    def all(
        self,
        table_name: str,
        column_values: Optional[List] = None,
        where_values: Optional[Union[Dict, str]] = None,
        *args,
        **_
    ) -> pyodbc.Cursor:
        """"""
        columns_sql = ','.join(column_values) if column_values else '*'
        where_sql = ''
        where_values_list = []
        if where_values:
            if isinstance(where_values, str):
                where_sql = where_values
            elif isinstance(where_values, dict):
                where_sql = self._get_assign_str(where_values, ' and ')
                where_values_list = where_values.values()

        sql = ' '.join([
            f'select {columns_sql}',
            f'from {table_name}',
            f'where {where_sql}' if where_sql else '',
        ])
        return self._execute(sql, *where_values_list, *args)

    def one(
        self,
        table_name: str,
        column_values: Optional[List] = None,
        where_values: Optional[Union[Dict, str]] = None,
        *args,
        **_
    ) -> pyodbc.Row:
        """"""
        return self.all(
            table_name, column_values, where_values, *args
        ).fetchone()

    def exists(
        self,
        table_name: str,
        where_values: Optional[Union[Dict, str]] = None,
        *args,
        **_
    ) -> bool:
        """"""
        return self.one(
            table_name, where_values=where_values, *args
        ) is not None

    def add(self, table_name: str, column_values: dict, *args, **_):
        """"""
        columns = ','.join(column_values.keys())
        values = '?, ' * len(column_values)
        sql = ' '.join([
            f'insert into {table_name}({columns})',
            f'values({values})',
        ])
        self._execute(sql, *column_values.values())

    def update(
        self,
        table_name: str,
        column_values: dict,
        where_values: dict,
        *args,
        **_
    ):
        """"""
        columns_sql = self._get_assign_str(column_values)
        where_sql = self._get_assign_str(where_values, ' and ')
        sql = ' '.join([
            f'update {table_name}',
            f'set {columns_sql}'
            f'where {where_sql}' if where_sql else '',
        ])
        self._execute(
            sql,
            *column_values.values(),
            *where_values.values(),
            *args
        )
