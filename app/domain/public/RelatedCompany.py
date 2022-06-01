from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class RelatedCompany:
    """
    Relacion entre empresas
    """

    RelatedCompanyID: int
    CompanyId: Ids.COMPANY_ID
    SubCompanyId: Ids.COMPANY_ID
    isActivate: bool = True
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
