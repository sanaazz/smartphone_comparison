from sqlalchemy import URL
from sqlalchemy import create_engine


def create_table(username, password, db_name):
    url_object = URL.create(
        "mysql+mysqlconnector",
        username=username,
        password=password,
        host="localhost",
        database=db_name
    )
    return create_engine(url_object)


def create_schema(username, password):
    url_object = URL.create('mysql+mysqlconnector',
                            username=username,
                            password=password,
                            host='localhost')
    return create_engine(url_object)
