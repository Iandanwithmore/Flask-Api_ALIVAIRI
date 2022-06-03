from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class ActivityExam:
    """
    Activity have many exams inside
    attr:
        ActivityExamId: serial int
        ActivityId: ForeignKey Activity, identifier of activity
        ExamId: ForeignKey Exam, identifier of exam
        Orden: when show or print this is the order
        CreateUserId: ForeignKey User, identifier of user that creates the register
        CreateDate: timestamp for audit purpose
    """

    ActivityExamId: int
    ActivityId: Ids.ACTIVITY_ID
    ExamId: Ids.EXAM_ID
    Orden: int
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
