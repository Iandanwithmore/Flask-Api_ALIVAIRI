from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class Option:
    """
    Options in system
    attr:
        OptionId: str with format define in Ids.py
        Description: name
        AppId: ForeignKey App, identifier of app
        pathSVG: path to file that contents svg image
        isActive: value to indicate state
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
        WriteUserId: ForeignKey User, identifier of user that modify the register
        WriteDate: timestamp for audit purpose
    """

    OptionId: Ids.OPTION_ID
    Description: str(100)
    AppId: Ids.APP_ID
    pathSVG: str(1500)
    isActivate: bool = True
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
