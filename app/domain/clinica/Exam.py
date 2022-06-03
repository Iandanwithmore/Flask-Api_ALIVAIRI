import app.domain.clinica.Constants as Constants
import app.domain.Ids as Ids

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Exam:
    """
    Set of indicator that fill doctor
    attr:
        ExamId: serial str with format define in Ids.py
        Description: title of exam
        Information: extra information about exam
        TypeServiceConstant: ForeignKey Constants (optional), services that provides hospital
        isActive: value to indicate state
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
        WriteUserId: ForeignKey User, identifier of user that modify the register
        WriteDate: timestamp for audit purpose
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
        return Constants.Service_TypeService.get(TypeServiceId)
