from dataclasses import dataclass
from datetime import datetime

import app.domain.clinica.Constants as Constants
import app.domain.Ids as Ids


@dataclass
class ScheduleActivity:
    """
    Conjunto de Examenes que se le aplicaran a una persona.
    """

    ScheduleActivityId: Ids.SCHEDULE_ACTIVITY_ID
    TypeConstant: str(1)
    EndDate: datetime.strptime("%d-%m-%Y") = None
    AdminEndDate: datetime.strptime("%d-%m-%Y") = None
    TypeTimeConstant: str(1)
    isActive: bool = False
    VoucherId: str(15)
    CompanyId: Ids.COMPANY_ID
    CompanyDistribution: Ids.COMPANY_DISTRIBUTION_ID
    Companyprofile: Ids.COMPANYPROFILE_ID
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()

    def get_TypeTimeConstant(self, TypeTimeConstant: str):
        return Constants.ScheduleActivity_LapseTime.get(TypeTimeConstant)
