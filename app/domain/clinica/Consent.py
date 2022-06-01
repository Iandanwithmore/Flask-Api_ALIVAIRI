import app.domain.Ids as Ids

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Consent:
    """
    Consentimientos para aplicar un examen
    """

    ConsentId: Ids.CONSENT_ID
    Description: str(40)
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
