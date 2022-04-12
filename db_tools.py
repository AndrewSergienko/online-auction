import sqlite3
from jinja2 import Template
from templates import Templates


class Database:
    con = None
    cur = None

    @classmethod
    def open_connection(cls):
        if not cls.con:
            cls.con = sqlite3.Connection('database.sqlite')
            cls.con.row_factory = sqlite3.Row
            cls.cur = cls.con.cursor()

    @classmethod
    def select(cls, context, fetchone=False):
        cls.open_connection()
        tm = Template(Templates.select)
        sql_request = tm.render(context)
        if fetchone:
            result = cls.cur.execute(sql_request).fetchone()
        else:
            result = cls.cur.execute(sql_request).fetchall()
        return result

    @classmethod
    def insert_into(cls, context):
        cls.open_connection()
        tm = Template(Templates.insert_into)
        sql_request = tm.render(context)
        cls.cur.execute(sql_request)
        cls.con.commit()

    @classmethod
    def get_foreign_keys(cls, table_name):
        cls.open_connection()
        sql_request = f"PRAGMA foreign_key_list({table_name})"
        return cls.cur.execute(sql_request).fetchall()

    @classmethod
    def close_connection(cls):
        cls.con.commit()
        cls.con.close()
        cls.con = cls.cur = None