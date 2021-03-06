import pymysql.cursors
from masonite.testing import TestCase
from .BaseGrammar import BaseGrammar


class SQLiteGrammar(BaseGrammar):

    """The keys in this dictionary is how the ORM will reference these aggregates

    The values on the right are the matching functions for the grammar

    Returns:
        [type] -- [description]
    """

    aggregate_options = {
        "SUM": "SUM",
        "MAX": "MAX",
        "MIN": "MIN",
        "AVG": "AVG",
        "COUNT": "COUNT",
        "AVG": "AVG",
    }

    type_map = {
        "string": "VARCHAR",
        "char": "CHARACTER",
        "integer": "INT",
        "big_integer": "BIGINT",
        "tiny_integer": "TINYINT",
        "big_increments": "BIGINT PRIMARY KEY AUTOINCREMENT",
        "small_integer": "SMALLINT",
        "medium_integer": "MEDIUMINT",
        "increments": "INT PRIMARY KEY AUTOINCREMENT",
        "binary": "BLOB",
        "boolean": "BOOLEAN",
        "decimal": "DECIMAL",
        "double": "DOUBLE",
        "enum": "VARCHAR",
        "text": "TEXT",
        "float": "FLOAT",
        "geometry": "TEXT",
        "json": "BLOB",
        "jsonb": "BLOB",
        "long_text": "TEXT",
        "point": "BLOB",
        "time": "REAL",
        "timestamp": "REAL",
        "date": "TEXT",
        "datetime": "TEXT",
        "year": "TEXT",
        "tiny_increments": "TINYINT AUTOINCREMENT",
        "unsigned": "INT UNSIGNED",
        "unsigned_integer": "INT UNSIGNED",
    }

    def select_format(self):
        return "SELECT {columns} FROM {table} {wheres} {group_by}{order_by}{limit}"

    def update_format(self):
        return "UPDATE {table} SET {key_equals} {wheres}"

    def insert_format(self):
        return "INSERT INTO {table} ({columns}) VALUES ({values})"

    def delete_format(self):
        return "DELETE FROM {table} {wheres}"

    def aggregate_string(self):
        return "{aggregate_function}({column}) AS {alias}"

    def key_value_string(self):
        return "{column} = '{value}'"

    def create_column_string(self):
        return "{column} {data_type}{length}{nullable}, "

    def create_start(self):
        return "CREATE TABLE {table} "

    def create_column_length(self):
        return "({length})"

    def table_string(self):
        return "`{table}`"

    def order_by_string(self):
        return "ORDER BY {column} {direction}"

    def column_string(self):
        return "`{column}`{seperator}"

    def value_string(self):
        return "'{value}'{seperator}"

    def limit_string(self):
        return "LIMIT {limit}"

    def first_where_string(self):
        return "WHERE"

    def additional_where_string(self):
        return "AND"
