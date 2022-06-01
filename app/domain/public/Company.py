from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class Company:
    """
    Examen que tiene asociado indicadores
    """

    CompanyId: Ids.COMPANY_ID
    Description: str(100)
    AddressId: Ids.CITYDISTRICT_ID
    Address: str(300)
    Password: str(128)
    isActivate: bool = True
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
