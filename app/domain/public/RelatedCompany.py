from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class RelatedCompany:
    """
    attr:
        RelatedCompanyID: serial int
        CompanyId: ForeignKey company, identifier of company
        SubCompanyId: ForeignKey company, identifier of company
        isActive: value to indicate state
        WriteUserId: ForeignKey User, identifier of user that modify the register
        WriteDate: timestamp for audit purpose
    """

    RelatedCompanyID: int
    CompanyId: Ids.COMPANY_ID
    SubCompanyId: Ids.COMPANY_ID
    isActivate: bool = True
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
