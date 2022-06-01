import psycopg2
from flask import current_app


class PlSql:
    def __init__(self):
        self.conn = None
        self.error = None
        self.data = None

    def connect(self, env="API_CONECTION"):
        lcConnect = current_app.config[env]
        try:
            self.conn = psycopg2.connect(lcConnect)
            return True
        except Exception as err:
            self.error = "EN CONEXION DB" + err
            raise self.error

    def Exec(self, lcSql):
        try:
            self.connect()
            with self.conn.cursor() as cur:
                cur.execute(lcSql)
                # laFila = cur.fetchone()
                # self.data = laFila[0]
                self.conn.commit()
                cur.close()
        except Exception as err:
            self.error = err
        if self.conn is not None:
            self.conn.close()

    def ExecRS(self, lcSql):
        try:
            self.connect()
            with self.conn.cursor() as cur:
                cur.execute(lcSql)
                self.data = cur.fetchall()
                self.conn.commit()
                cur.close()
        except Exception as err:
            self.error = err
        if self.conn is not None:
            self.conn.close()
