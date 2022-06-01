from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class App:
    """
    Examen que tiene asociado indicadores
    """

    AppId: Ids.APP_ID
    Description: str(100)
    Version: decimal
    isActive: bool = False
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
