from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class ScheduleActivityConsent:
    """
    Puente entre consentimiento y plan de la actividad
    """

    ScheduleActivityConsentId: int
    ScheduleActivityId: Ids.SCHEDULE_ACTIVITY_ID
    ConsentId: Ids.CONSENT_ID
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
