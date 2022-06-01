from domain import Exam

from app.infrastructure.PlSql import PlSql
from app.services.ActivityRepositoryInterface import ActivityRepositoryInterface

loPsql = PlSql()
aExam = list[Exam]


class ExamRepository(ExamRepositoryInterface):
    def get_by_activyid(self, id: str) -> aExam:
        pass
