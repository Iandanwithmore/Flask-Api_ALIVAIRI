from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class CityDistrict:
    """
    Examen que tiene asociado indicadores
    """

    CityDistrictId: Ids.CITYDISTRICT_ID
    Description: str(45)
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
