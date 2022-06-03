from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class ActivityCie10:
    """
    Complement to Activity in base of dataset of diagnostics that gives the state (Peru)
    attr:
        ActivityCie10Id: serial int
        ActivityId: ForeignKey Activity, identifier of activity
        Cie10Id: ForeignKey Cie10, identifier of cie10
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
    """

    ActivityCie10Id: int
    # ScheduleActivityId: Ids.SCHEDULE_ACTIVITY_ID
    ActivityId: Ids.ACTIVITY_ID
    Cie10Id: Ids.CIE10_ID
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
