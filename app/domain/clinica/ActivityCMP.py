from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class ActivityCMP:
    """
    Opcional: Puente entre actividad y CMP(Codigo medico procedimental)
    """

    ActivityCMPId: int
    # ScheduleActivityId: Ids.SCHEDULE_ACTIVITY_ID
    ActivityId: Ids.ACTIVITY_ID
    CMPId: Ids.CMP_ID
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
