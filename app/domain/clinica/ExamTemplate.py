from datetime import datetime

import app.domain.Ids as Ids


class ExamTemplate:
    """
    Plantilla que tiene el orden de los indicadores
    attr:
        ExamTemplateId: serial int
        ExamId: ForeignKey Exam, identifier of exam
        IndicatorID: ForeignKey Indicator, identifier of Indicator
        OrderLinkedList: order for subtitle and idicators
        WriteUserId: ForeignKey User, identifier of user that modify the register
        WriteDate: timestamp for audit purpose
    """

    ExamTemplateId: int
    ExamId: Ids.CONSENT_ID
    IndicatorID: Ids.INDICATOR_ID
    OrderLinkedList: str(6)
    WriteUserId: Ids.USER_ID
    WriteDate: datetime = datetime.now()
