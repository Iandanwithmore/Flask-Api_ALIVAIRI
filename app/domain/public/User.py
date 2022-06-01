from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class User:
    """
    Opciones del sistema
    """

    UserId: Ids.USER_ID
    PersonId: Ids.PERSON_ID
    isActivate: bool = True
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
