from sqlite3 import *
from data.config import DATABASE


class DBApi(object):

    def __init__(self) -> None:
        self.__conn: Connection = connect(DATABASE)
        self.__cur: Cursor = self.__conn.cursor()

    async def create_users_table(self) -> None:
        """CREATE USER TABLES"""
        self.__cur.execute('''
            CREATE TABLE IF NOT EXISTS users2 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_post	INTEGER,
            name_post TEXT,
            id_user	INTEGER,
            txt_user_comment TEXT,
            "username" TEXT
        );
        ''')
        self.__conn.commit()

    async def delete_table(self):
        self.__cur.execute('''
                    DROP TABLE users2
                ''')
        self.__conn.commit()

    async def add_user(self, id_post: int, text_post: str, id_user: int, txt_user_comment: str, username: str) -> bool:
        """ADD NEW USERS"""
        try:
            self.__cur.execute('''
                INSERT INTO
                users2(
                    id_post,
                    name_post,
                    id_user,
                    txt_user_comment,
                    username
                )
                VALUES(?, ?, ?, ?, ?)
            ''', (id_post, text_post, id_user, txt_user_comment, username))
            self.__conn.commit()
        except IntegrityError:
            return False
        else:
            return True

    async def add_user2(self, id_post, name_post, id_user: int, txt_user_comment: str, username: str) -> bool:
        """ADD NEW USERS"""
        try:
            self.__cur.execute('''
                INSERT INTO
                users2(
                    id_post,
                    name_post,
                    id_user,
                    txt_user_comment,
                    username
                )
                VALUES(?,?, ?, ?,?)
            ''', (id_post,name_post, id_user, txt_user_comment, username))
            self.__conn.commit()
        except IntegrityError:
            return False
        else:
            return True

    async def update_user(self, id_user: int, txt_user_comment: str, username: str, id_post: int) -> None:
        self.__cur.execute('''
            UPDATE users
            SET id_user = ?, txt_user_comment = ?, username = ?
            WHERE id_post = ?
        ''', (id_user, txt_user_comment, username, id_post))
        self.__conn.commit()

    async def count_users(self, id_post: str):
        result = f'SELECT COUNT(*) FROM users2 WHERE id_post = "{id_post}"'
        return self.__cur.execute(result).fetchone()

    async def user_winner(self, id: int, id_post: str):
        result = f'SELECT username, txt_user_comment FROM users2 WHERE id = {id} and id_post = "{id_post}"'
        return self.__cur.execute(result).fetchall()

    async def get_id_post(self):
        result = f'SELECT id_post FROM users2 WHERE id = 1'
        return self.__cur.execute(result).fetchall()

    async def create_all_database(self) -> None:
        """CREATE DATABASE"""
        #await self.create_users_table()
