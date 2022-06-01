from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class RoleOption:
    """
    Opciones del sistema
    """

    RoleOptionId: int
    RoleId: Ids.ROLE_ID
    OptionId: Ids.OPTION_ID
    isActive: bool = True
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
