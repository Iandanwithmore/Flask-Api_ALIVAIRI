import app.domain.clinica.Constants as Constants
import app.domain.Ids as Ids

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Exam:
    """
    Examen que tiene como sub conjunto indicadores
    """

    ExamId: Ids.EXAM_ID
    Description: str(200)
    Information: str(900)
    TypeServiceConstant: str(1)
    isActive: bool = False
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
    # AsociateExamID: str

    def get_TypeServiceConstant(self, TypeServiceId: str):
        return Constants.ConstantService_TypeService.get(TypeServiceId)
