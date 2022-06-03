from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids
import app.domain.clinica.Constants as Constants


@dataclass
class Indicator:
    """
    Indicador de un examen
    """

    IndicatorId: Ids.INDICATOR_ID
    Information: str(300)
    Description: str(300)
    Default: str(1)
    Range: str(400)
    Unit: str(50)
    isActive: bool = True
    TypeFieldConstant: str(1)
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()

    def get_TypeFieldConstant(self, TypeofFieldConstant: str):
        return Constants.Service_TypeService.get(TypeofFieldConstant)
