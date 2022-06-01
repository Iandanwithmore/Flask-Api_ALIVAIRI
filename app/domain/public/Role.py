from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class Role:
    """
    Opciones del sistema
    """

    RoleId: Ids.ROLE_ID
    Description: str(100)
    AppId: Ids.APP_ID
    pathSVG: str(1500)
    isActivate: bool = True
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
