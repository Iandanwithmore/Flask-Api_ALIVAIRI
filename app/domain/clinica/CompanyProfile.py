from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class CompanyProfile:
    """
    Perfilq ue contiene examenes de una empresa
    """

    CompanyprofileId: Ids.COMPANYPROFILE_ID
    Description: str(50)
    CompanyId: Ids.COMPANY_ID
    isActive: bool = False
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
