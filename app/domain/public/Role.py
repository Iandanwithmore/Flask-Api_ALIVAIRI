from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class Role:
    """
    Set of Options
    attr:
        RoleId: serial str with format define in Ids.py
        Description: name
        pathSVG: path to file that contents svg image
        isActive: value to indicate state
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
        WriteUserId: ForeignKey User, identifier of user that modify the register
        WriteDate: timestamp for audit purpose
    """

    RoleId: Ids.ROLE_ID
    Description: str(100)
    pathSVG: str(1500)
    isActivate: bool = True
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
