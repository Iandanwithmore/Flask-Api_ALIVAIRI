from domain import Activity

from app.decorators import exception_handler
from app.infrastructure.PlSql import PlSql
from app.services.ActivityRepositoryInterface import ActivityRepositoryInterface
from app.services.Response import ResponseInterface

loPsql = PlSql()


class ActivityRepository(ActivityRepositoryInterface):
    def __init__(self):
        self.response = ResponseInterface()

    @exception_handler
    def get_by_id(self, Activityid: str):
        data = []
        query_str = f"SELECT * FROM clinica.Activity WHERE ActivityId = '{Activityid}'"
        loPsql.ExecRS(query_str)
        assert loPsql.data is None or len(loPsql.data) == 0, f"RESPUESTA VACIA"
        for item in loPsql.dat:
            data.append(Activity(item).__dict__)
