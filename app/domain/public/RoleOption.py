from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class RoleOption:
    """
    Relation role and option
    attr:
        RoleOptionId: serial int
        RoleId: ForeignKey Role, identifier of role
        OptionId: ForeignKey Option, identifier of option
        isActive: value to indicate state
        WriteUserId: ForeignKey User, identifier of user that modify the register
        WriteDate: timestamp for audit purpose
    """

    RoleOptionId: int
    RoleId: Ids.ROLE_ID
    OptionId: Ids.OPTION_ID
    isActive: bool = True
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
