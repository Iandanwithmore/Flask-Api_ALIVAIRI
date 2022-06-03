from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class UserRole:
    """
    Relation User and Rol
    attr:
        UserRoleId: serial int
        UserId: ForeignKey User, identifier of user
        RoleId: ForeignKey Role, identifier of role
        level: level in system is use in option to do things
        isActive: value to indicate state
        WriteUserId: ForeignKey User, identifier of user that modify the register
        WriteDate: timestamp for audit purpose
    """

    UserRoleId: int
    UserId: Ids.USER_ID
    RoleId: Ids.ROLE_ID
    level: int
    isActive: bool = True
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
