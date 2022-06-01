from datetime import datetime

import app.domain.Ids as Ids


class ExamSubtitle:
    """
    Subitulos presentes en los PDF para agrupar indicadores
    """

    ExamSubtitleId: int
    ExamId: Ids.CONSENT_ID
    OrderLinkedList: str(6)
    CreateUserId: Ids.USER_ID
    CreateDate: datetime = datetime.now()
