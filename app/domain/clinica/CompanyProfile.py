from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class CompanyProfile:
    """
    Company have many profiles that includes many exams
    attr:
        CompanyprofileId: serial str
        Description: name of Profile
        CompanyId: ForeignKey Company, identifier of company
        isActive: bool = False
        CreateUserId: Ids.USER_ID
        CreateDate: datetime = datetime.now()
        WriteUserId: Ids.USER_ID
        WriteDate: datetime = datetime.now()
    """

    CompanyprofileId: Ids.COMPANYPROFILE_ID
    Description: str(50)
    CompanyId: Ids.COMPANY_ID
    isActive: bool = False
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
