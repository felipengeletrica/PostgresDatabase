import psycopg2 as pg
from __builtin__ import str


class postgres(object):

    def __init__(self, host, database, user, password, autocommit=True):

        """
        :type host: address database server
        :type database: database name
        :type user: username
        :type user: password
        :return: boolean
        """
        
        try:
            self.conn_string = \
                "host='" + host + \
                "' dbname='" + database + \
                "' user='" + user + \
                "' password='" + password + "'"

            self.autocommit_mode = bool(autocommit)
            self.conn = pg.connect(self.conn_string)
            self.cursor = self.conn.cursor()

            #self.conn = None
            #self.cursor = None

        except:
            raise

    def query(self, sql):

        """
        :type sql: Query
        :return: data in list
        """
        try:

            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except:
            raise
            result = None
        return result

    def insert(self, sql, commit=True):
        """
        :type sql: SQL string
        :type commit: bool
        :return: int. The row id of the insert. if query contains RETURNING 'id'
        """
        try:
            self.cursor.execute(sql)
            if commit:
                self.conn.commit()

            if "RETURNING" in sql:
                return self.cursor.fetchone()[0]
            return None

        except:
            raise

    def select(self, query):

        """
        :type query: Query
        :return: data in list
        """
        try:
            self.cur.execute(query)
            return self.cur.fetchall()
        except:
            raise

    def connect(self):

        """
        :return: true or false in reconecting
        """
        try:
            self.conn = pg.connect(self.conn_string)
            self.cursor = self.conn.cursor()
            return True
        except:
            pass
        return False

    def disconnect(self):
        """
        :return: true or false in disconect
        """
        try:
            if self.conn:
                self.conn.close()
                return True
            return False
        except:
            pass