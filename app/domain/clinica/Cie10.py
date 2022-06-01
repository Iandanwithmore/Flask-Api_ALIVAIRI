from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class Cie10:
    """
    Codigos del estado peruano para el diagnostico
    """

    Cie10Id: Ids.CIE10_ID
    Description: str(300)
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
