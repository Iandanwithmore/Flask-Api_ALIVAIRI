from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class CityDepartment:
    """
    Examen que tiene asociado indicadores
    """

    CityDepartmentId: Ids.CITYDEPARTMENT_ID
    Description: str(30)
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
