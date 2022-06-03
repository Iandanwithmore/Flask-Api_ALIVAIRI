from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class User:
    """
    Person with privilegies in app
    attr:
        UserId: serial str with format define in Ids.py
        PersonId: ForeignKey PErson, identifier of person
        isActive: value to indicate state
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
        WriteUserId: ForeignKey User, identifier of user that modify the register
        WriteDate: timestamp for audit purpose
    """

    UserId: Ids.USER_ID
    PersonId: Ids.PERSON_ID
    isActivate: bool = True
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
