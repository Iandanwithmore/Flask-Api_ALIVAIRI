import psycopg2
from ..config import Config

class PlSql:
    def __init__(self):
        self.conn = None
        self.error = None
        self.data = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(Config["PSQL_DB_CONECTION"])
            return True
        except Exception as err:
            self.error = "EN CONEXION DB" + err
            raise self.error

    def Exec(self, query:str):
        try:
            self.connect()
            with self.conn.cursor() as cur:
                cur.execute(query)
                # laFila = cur.fetchone()
                # self.data = laFila[0]
                self.conn.commit()
                cur.close()
        except Exception as err:
            self.error = err
        if self.conn is not None:
            self.conn.close()

    def ExecRS(self, query:str):
        try:
            self.connect()
            with self.conn.cursor() as cur:
                cur.execute(query)
                self.data = cur.fetchall()
                self.conn.commit()
                cur.close()
        except Exception as err:
            self.error = err
        if self.conn is not None:
            self.conn.close()
