from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class CompanyProfileExam:
    """
    Puente Perfiles examenes
    """

    CompanyprofileExamId: int
    CompanyprofileId: Ids.COMPANY_ID
    ExamId: Ids.EXAM_ID
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
