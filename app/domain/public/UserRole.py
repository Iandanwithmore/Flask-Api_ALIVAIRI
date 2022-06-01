from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class UserRole:
    """
    Opciones del sistema
    """

    UserRoleId: int
    UserId: Ids.USER_ID
    RoleId: Ids.ROLE_ID
    level: int
    isActive: bool = True
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
