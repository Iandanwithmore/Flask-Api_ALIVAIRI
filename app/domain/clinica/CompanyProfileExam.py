from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class CompanyProfileExam:
    """
    Perfil have many exams inside
    attr:
        CompanyprofileExamId: serial int
        CompanyprofileId: ForeignKey Companyprofile, identifier of profile
        ExamId: ForeignKey Exam, identifier of exam
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
    """

    CompanyprofileExamId: int
    CompanyprofileId: Ids.COMPANY_ID
    ExamId: Ids.EXAM_ID
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
