from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class Cie10:
    """
    From https://www.datosabiertos.gob.pe/dataset/cie-x Peru
    attr:
        Cie10Id: id define by dataset
        Description: diagnostic
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
    """

    Cie10Id: Ids.CIE10_ID
    Description: str(300)
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
