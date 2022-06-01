from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class ActivityDetail:
    """
    Llenado de indicadores con respecto a los examenes de una actividad
    """

    ActivityDetailId: int
    ScheduleActivityId: Ids.SCHEDULE_ACTIVITY_ID
    ActivityId: Ids.SCHEDULE_ACTIVITY_ID
    IndicatorId: Ids.INDICATOR_ID
    SelectedOptionfromConstants: int
    Result: str(800)
    isActive: bool = False
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
