from datetime import datetime

import app.domain.Ids as Ids


class ExamTemplate:
    """
    Plantilla que tiene el orden de los indicadores
    """

    ExamTemplateId: int
    ExamId: Ids.CONSENT_ID
    IndicatorID: Ids.INDICATOR_ID
    OrderLinkedList: str(6)
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
