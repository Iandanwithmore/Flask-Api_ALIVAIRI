from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class App:
    """
    Apps Register
    attr:
        AppId: serail int
        Description: title of app
        Version: information about dev of app
        isActive: value to indicate state
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
        WriteUserId: ForeignKey User, identifier of user that modify the register
        WriteDate: timestamp for audit purpose
    """

    AppId: Ids.APP_ID
    Description: str(100)
    Version: decimal
    isActive: bool = False
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
