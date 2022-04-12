import os
import hashlib
import bcrypt
import sqlite3
from datetime import datetime

from db_tools import Database


class Model:
    # Поле, яке потрібне для запитів в базу, в данному випадку використовується як заглушка для зролумілості коду.
    # Перегружається в класах-потомках.
    table_name = 'model'

    # Поля моделі, які будуть ініціалізовані в конструкторі класів нащадків
    fields = []

    def __init__(self, **kwargs):
        for field in type(self).fields:
            # if field in kwargs.keys():
            #     self.__dict__[field] = kwargs[field]
            # else:
            #     self.__dict__[field] = None
            self.__dict__[field] = kwargs[field] if field in kwargs.keys() else None

    @classmethod
    def all(cls):
        # Метод повертає список всих об'єктів моделі, які формуються з рядків таблиці
        models_objects = []
        context = {'table_name': cls.table_name}
        data = Database.select(context)
        for row in data:
            # Клас Model наслідується класами, в конструкторі яких є варіант з update'ом словника властивостей
            # Тому, можна передавати параметром словник при створенні об'єкта
            model_object = cls(**row)
            # Засетить об'єкти рядку класів, з якими пов'язані зовнішні ключі
            cls.set_fk_fields(model_object)
            models_objects.append(model_object)
        Database.close_connection()
        return models_objects

    @classmethod
    def set_fk_fields(cls, model_object):
        # Метод створює об'єкти класів рядка таблиці, до якого належить конкретний зовнішній ключ
        # і сетить їх об'єкту головної моделі

        # Знаходить всі зовнішні ключі таблиці.
        f_keys = Database.get_foreign_keys(cls.table_name)

        for key in f_keys:
            # f_keys отримується за допомогою запросу PRAGMA foreign_key_list(<Таблиця>), який повертає такі дані:
            # table, from, to. Кожен рядок позначає один зовнішній ключ.
            # table - таблиця-джерело, до поля якої прив'язаний ключ
            # from - поле поточної таблиці, яке прив'язано до ключа
            # to - поле таблиці-джерела

            # Записується клас таблиці-джерела для подальшого створення об'єкту і записування в головну модель
            fk_class = table_classes[key['table']]
            row_name = key['from']
            reference_name = key['to']
            # Отримується рядок таблиці-джерела по умові співпадіння зі значенням поля
            row_value = Database.select({'table_name': key['table'],
                                         'where_condition': f'{reference_name}={model_object.__dict__[row_name]}'},
                                        fetchone=True)
            # Клас Model наслідується класами, в конструкторі яких є варіант з update'ом словника властивостей
            # Тому, можна передавати параметром словник при створенні об'єкта
            model_object.__dict__[row_name] = fk_class(**row_value)

    @classmethod
    def get(cls, **kwargs):
        # Повертає один об'єкт моделі, який задовільняє умові(ам).
        # Рядок condition буде сформований наступним циклом і буде підставленний в SQL запрос
        condition = ''
        for key in kwargs.keys():
            # При виклику метода потрібно використовувати префіксні вирази, які допомагають сформувати SQL запрос
            # and__condition -> ... AND condition
            # or__condition -> ... OR condition
            # префіксний вираз не потрібно лиш вказувати в первому параметрі.
            if '__' in key:
                oper = 'OR' if 'or__' in key else 'AND'
                clear_key = key.replace('or__', "").replace('and__', '')
                condition += f' {oper} {clear_key}={kwargs[key]}'
            else:
                condition += f"{key}=\'{kwargs[key]}\'"

        context = {'table_name': cls.table_name, 'where_condition': condition}

        # Database.select поверне словник полів одного рядку, це забеспечує параметер fetchone
        # Клас Model наслідується класами, в конструкторі яких є варіант з update'ом словника властивостей
        # Тому, можна передавати параметром словник при створенні об'єкта.
        model_object = cls(**Database.select(context, fetchone=True))
        # Засетить об'єкти рядку класів, з якими пов'язані зовнішні ключі
        cls.set_fk_fields(model_object)
        return model_object

    def save(self):
        context = {
            'table_name': type(self).table_name,
            'fields': ", ".join(self.__dict__.keys()),
            'values': ", ".join(map(lambda x: f'\'{x}\'', self.__dict__.values()))
        }
        Database.insert_into(context)


class Lot(Model):
    table_name = 'lots'
    fields = ['id', 'seller', 'title', 'description', 'min_bid', 'cur_bid', 'cur_buyer', 'start_time', 'start_date',
              'end_time', 'end_date', 'picture_path']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_time_object()

    def create_time_object(self):
        self.start_object_time = datetime.strptime(f"{self.start_date} {self.start_time}", "%d.%m.%Y %H:%M")
        self.end_object_time = datetime.strptime(f"{self.end_date} {self.end_time}", "%d.%m.%Y %H:%M")


class User(Model):
    table_name = 'users'
    fields = ['id', 'username', 'password', 'firstname', 'lastname', 'phone_number']

    def set_password(self, pw):
        pw = pw.encode('utf-8')
        self.password = bcrypt.hashpw(pw, bcrypt.gensalt(10)).decode()

    def check_password(self, pw):
        pw = pw.encode('utf-8')
        return bcrypt.checkpw(pw, self.password.encode('utf-8'))

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


table_classes = {
    'model': Model,
    'lots': Lot,
    'users': User
}