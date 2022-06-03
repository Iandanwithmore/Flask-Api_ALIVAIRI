from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class CityProvince:
    """
    Second Subclass of District ID of City base on (Department-Province-Disctrict) Ubigeo from Peru
    attr:
        CityDepartmentId: id from dataset
        Description: city name
        WriteUserId: ForeignKey User, identifier of user that modify the register
        WriteDate: timestamp for audit purpose
    """

    CityProvinceId: Ids.CITYPROVINCE_ID
    Description: str(45)
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
