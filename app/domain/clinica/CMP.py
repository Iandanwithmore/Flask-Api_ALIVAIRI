from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class CMP:
    """
    From https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjw3eaX2ZH4AhVoBbkGHbu4Dz0QFnoECAgQAQ&url=https%3A%2F%2Fdocs.bvsalud.org%2Fbiblioref%2F2020%2F05%2F1095757%2Frm_243-2020-minsa.pdf&usg=AOvVaw0rijJ8k7CHWsWKYiKPwnGl Peru
    attr:
        CMPId: id define by dataset
        Description: medical procedure
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
    """

    CMPId: Ids.CMP_ID
    Description: str(20000)
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
