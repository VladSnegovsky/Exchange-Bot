import os
import psycopg2
from contextlib import closing

import Config

def create_table():
    with closing(psycopg2.connect(database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASS, host=Config.DB_HOST, port=Config.DB_PORT)) as connection:
        with connection.cursor() as cursor:
            cursor.execute('CREATE TABLE users (ID BIGSERIAL PRIMARY KEY, user_ID BIGINT, time INTEGER, info TEXT);')
            connection.commit()

def user_exists(user_id):
    """Check if there is already a user in the database"""
    with closing(psycopg2.connect(database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASS, host=Config.DB_HOST, port=Config.DB_PORT)) as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM users WHERE user_ID = %s', (user_id,))
            result = cursor.fetchall()
            return bool(len(result))

def add_user(user_id):
    """Adding new user"""
    with closing(psycopg2.connect(database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASS, host=Config.DB_HOST, port=Config.DB_PORT)) as connection:
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO users (user_id, time, info) VALUES (%s, %s, %s)', (user_id, 0, "NoData"))
            connection.commit()

def update_info(user_id, time, info):
    """Update info of user"""
    with closing(psycopg2.connect(database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASS, host=Config.DB_HOST, port=Config.DB_PORT)) as connection:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE users SET time = %s, info = %s WHERE user_id = %s", (time, info, user_id))
            connection.commit()

def get_time(user_id):
    """Returns time"""
    with closing(psycopg2.connect(database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASS, host=Config.DB_HOST, port=Config.DB_PORT)) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT time FROM users WHERE user_id = %s", (user_id,))
            result = cursor.fetchall()
            return result

def get_info(user_id):
    """Returns info"""
    with closing(psycopg2.connect(database=Config.DB_NAME, user=Config.DB_USER, password=Config.DB_PASS, host=Config.DB_HOST, port=Config.DB_PORT)) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT info FROM users WHERE user_id = %s", (user_id,))
            result = cursor.fetchall()
            return result