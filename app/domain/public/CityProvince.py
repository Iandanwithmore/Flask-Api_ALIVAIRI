from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class CityProvince:
    """
    Examen que tiene asociado indicadores
    """

    CityProvinceId: Ids.CITYPROVINCE_ID
    Description: str(45)
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
