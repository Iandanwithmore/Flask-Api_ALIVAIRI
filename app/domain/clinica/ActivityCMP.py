from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class ActivityCMP:
    """
    Complement to Activity in base of dataset of medical procedure that gives the state (Peru)
    attr:
        ActivityCMPId: serial int
        ActivityId: ForeignKey Activity, identifier of activity
        CMPId: ForeignKey CMP, identifier of cmp
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
    """

    ActivityCMPId: int
    # ScheduleActivityId: Ids.SCHEDULE_ACTIVITY_ID
    ActivityId: Ids.ACTIVITY_ID
    CMPId: Ids.CMP_ID
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
