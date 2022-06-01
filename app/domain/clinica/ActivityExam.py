from dataclasses import dataclass
from datetime import datetime

import app.domain.Ids as Ids


@dataclass
class ActivityExam:
    """
    Puente entre actividad y examen
    """

    ActivityExamId: int
    ActivityId: Ids.ACTIVITY_ID
    ExamId: Ids.EXAM_ID
    Orden: int
    Grupo: int
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
