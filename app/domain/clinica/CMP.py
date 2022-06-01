from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class CMP:
    """
    Codigos del estado peruano para el procedimientos medicos
    """

    Cie10Id: Ids.CMP_ID
    Description: str(20000)
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
