from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class ActivityDetail:
    """
    Where indicators are fill respect from activity (many exams)
    attr:
        ActivityDetailId: serial int
        ScheduleActivityId: ForeignKey ScheduleActivity, identifier of schedule of activity
        ActivityId: ForeignKey Activity, identifier of activity
        IndicatorId: ForeignKey Indicator, identifier of indicator of exam
        SelectedOptionfromConstants: ForeignKey Constants (optional), when field is select save position of this option
        Result: result for field of exam
        ExamTemplateId: ForeignKey ExamTemplate, identifier of template
        isActive: value to indicate state
        WriteUserId: ForeignKey User, identifier of user that modify the register
        WriteDate: timestamp for audit purpose
    """

    ActivityDetailId: int
    #ScheduleActivityId: Ids.SCHEDULE_ACTIVITY_ID
    ActivityId: Ids.SCHEDULE_ACTIVITY_ID
    IndicatorId: Ids.INDICATOR_ID
    SelectedOptionfromConstants: int
    Result: str(800)
    ExamTemplateId: Ids.EXAMTEMPLATE_ID
    isActive: bool = False
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
