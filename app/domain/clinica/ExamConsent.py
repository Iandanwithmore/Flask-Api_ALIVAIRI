import app.domain.Ids as Ids

from dataclasses import dataclass
from datetime import datetime


@dataclass
class ExamConsent:
    """
    title of document generated for apply exam to a person
    attr:
        ExamConsentId: ñserial int
        Description: title of consent
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
    """

    ExamConsentId: Ids.CONSENT_ID
    Description: str(40)
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
