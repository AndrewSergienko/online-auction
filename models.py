import sqlite3

from db_tools import Database


class Model:
    # Поле, яке потрібне для запитів в базу, в данному випадку використовується як заглушка для зролумілості коду.
    # Перегружається в класах-потомках.
    table_name = 'model'

    @classmethod
    def all(cls):
        # Метод повертає список всих об'єктів моделі, які формуються з рядків таблиці
        models_objects = []
        context = {'table_name': cls.table_name}
        data = Database.select(context)
        for row in data:
            # Клас Model наслідується класами, в конструкторі яких є варіант з update'ом словника властивостей
            # Тому, можна передавати параметром словник при створенні об'єкта
            model_object = cls(row)
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
            model_object.__dict__[row_name] = fk_class(row_value)

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
                oper = 'or__' if 'or__' in key else 'and__'
                clear_key = key.replace(oper, "")
                condition += f' OR {clear_key}={kwargs[key]}'
            else:
                condition += f"{key}={kwargs[key]}"

        context = {'table_name': cls.table_name, 'where_condition': condition}

        # Database.select поверне словник полів одного рядку, це забеспечує параметер fetchone
        # Клас Model наслідується класами, в конструкторі яких є варіант з update'ом словника властивостей
        # Тому, можна передавати параметром словник при створенні об'єкта.
        model_object = cls(Database.select(context, fetchone=True))
        # Засетить об'єкти рядку класів, з якими пов'язані зовнішні ключі
        cls.set_fk_fields(model_object)
        return model_object


class Lot(Model):
    table_name = 'lots'

    def __init__(self, args_dict=None, seller=None, title=None, description=None, min_bid=None, cur_bid=None,
                 cur_buyer=None, start_time=None, start_date=None, end_time=None, end_date=None):
        if args_dict and type(args_dict) == sqlite3.Row:
            self.__dict__.update(args_dict)
        else:
            self.seller = seller
            self.title = title
            self.description = description
            self.min_bid = min_bid
            self.cur_bid = cur_bid
            self.cur_buyer = cur_buyer
            self.start_time = start_time
            self.start_date = start_date
            self.end_time = end_time
            self.end_date = end_date


class User(Model):
    table_name = 'users'

    def __init__(self, args_dict=None, first_name=None, last_name=None, phone_number=None):
        if args_dict and type(args_dict) == sqlite3.Row:
            self.__dict__.update(args_dict)
        else:
            self.first_name = first_name
            self.last_name = last_name
            self.phone_number = phone_number


table_classes = {
    'model': Model,
    'lots': Lot,
    'users': User
}