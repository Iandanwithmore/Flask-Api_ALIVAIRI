from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class ActivityCie10:
    """
    Opcional: Puente entre actividad y Cie10
    """

    ActivityCie10Id: int
    # ScheduleActivityId: Ids.SCHEDULE_ACTIVITY_ID
    ActivityId: Ids.ACTIVITY_ID
    Cie10Id: Ids.CIE10_ID
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
